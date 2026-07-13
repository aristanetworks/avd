# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# ruff: noqa: INP001
from __future__ import annotations

import argparse
import json
import posixpath
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

LINK_ATTRS = {
    "a": ("href",),
    "area": ("href",),
    "audio": ("src",),
    "embed": ("src",),
    "iframe": ("src",),
    "img": ("src", "srcset"),
    "link": ("href",),
    "object": ("data",),
    "script": ("src",),
    "source": ("src", "srcset"),
    "track": ("src",),
    "video": ("poster", "src"),
}


@dataclass(frozen=True)
class Link:
    source: Path
    target: str
    line: int
    attribute: str


class BuiltDocsParser(HTMLParser):
    def __init__(self, source: Path) -> None:
        super().__init__(convert_charrefs=True)
        self.source = source
        self.anchors: set[str] = set()
        self.links: list[Link] = []
        self._in_config_script = False
        self._config_script_data: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {name: value for name, value in attrs if value is not None}

        if tag == "script" and attrs_dict.get("id") == "__config":
            self._in_config_script = True
            self._config_script_data = []

        for anchor_attr in ("id", "name"):
            if anchor_attr in attrs_dict:
                self.anchors.add(attrs_dict[anchor_attr])

        for attr in LINK_ATTRS.get(tag, ()):
            value = attrs_dict.get(attr)
            if not value:
                continue
            if attr == "srcset":
                self.links.extend(Link(self.source, target, self.getpos()[0], attr) for target in srcset_urls(value))
            else:
                self.links.append(Link(self.source, value, self.getpos()[0], attr))

    def handle_data(self, data: str) -> None:
        if self._in_config_script:
            self._config_script_data.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag != "script" or not self._in_config_script:
            return
        self._in_config_script = False
        try:
            config = json.loads("".join(self._config_script_data))
        except json.JSONDecodeError:
            return
        search_worker = config.get("search")
        if isinstance(search_worker, str):
            self.links.append(Link(self.source, search_worker, self.getpos()[0], "script#__config.search"))


def srcset_urls(srcset: str) -> list[str]:
    urls: list[str] = []
    for srcset_candidate in srcset.split(","):
        stripped_candidate = srcset_candidate.strip()
        if not stripped_candidate:
            continue
        urls.append(stripped_candidate.split()[0])
    return urls


def is_internal_url(url: str) -> bool:
    parsed = urlsplit(url)
    return not parsed.scheme and not parsed.netloc


def resolve_target(site_dir: Path, source: Path, target: str) -> tuple[Path, str]:
    parsed = urlsplit(target)
    fragment = unquote(parsed.fragment)
    path = unquote(parsed.path)

    if not path:
        return source, fragment

    if path.startswith("/"):
        relative_target = PurePosixPath(path.removeprefix("/"))
    else:
        source_relative_dir = source.relative_to(site_dir).parent.as_posix()
        relative_target = PurePosixPath(posixpath.normpath(posixpath.join(source_relative_dir, path)))

    if relative_target.as_posix() in {"", "."}:
        relative_target = PurePosixPath("index.html")
    elif path.endswith("/"):
        relative_target /= "index.html"

    return site_dir / Path(relative_target), fragment


def parse_html_files(site_dir: Path, ignored_html_patterns: list[str]) -> tuple[dict[Path, set[str]], list[Link]]:
    anchors_by_file: dict[Path, set[str]] = {}
    links: list[Link] = []
    for html_file in sorted(site_dir.rglob("*.html")):
        html_file_relative = html_file.relative_to(site_dir).as_posix()
        if any(PurePosixPath(html_file_relative).match(pattern) for pattern in ignored_html_patterns):
            continue
        parser = BuiltDocsParser(html_file)
        parser.feed(html_file.read_text(encoding="utf-8"))
        anchors_by_file[html_file] = parser.anchors
        links.extend(parser.links)
    return anchors_by_file, links


def format_path(path: Path, site_dir: Path) -> str:
    try:
        return path.relative_to(site_dir).as_posix()
    except ValueError:
        return path.as_posix()


def check_links(site_dir: Path, *, check_anchors: bool, ignored_html_patterns: list[str]) -> list[str]:
    anchors_by_file, links = parse_html_files(site_dir, ignored_html_patterns)
    errors: list[str] = []

    for link in links:
        if not is_internal_url(link.target):
            continue

        target_path, fragment = resolve_target(site_dir, link.source, link.target)
        if not target_path.exists():
            errors.append(
                f"{format_path(link.source, site_dir)}:{link.line}: {link.attribute} points to missing file {link.target!r} "
                f"(resolved as {format_path(target_path, site_dir)!r})"
            )
            continue

        if check_anchors and fragment and target_path.suffix == ".html" and fragment not in anchors_by_file.get(target_path, set()):
            errors.append(
                f"{format_path(link.source, site_dir)}:{link.line}: {link.attribute} points to missing anchor {link.target!r} "
                f"in {format_path(target_path, site_dir)!r}"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check internal links in a built MkDocs site.")
    parser.add_argument("site_dir", type=Path, help="Path to the built site directory.")
    parser.add_argument(
        "--check-anchors",
        action="store_true",
        help="Also validate URL fragments against anchors in generated HTML. This is disabled by default until existing generated ## links are fixed.",
    )
    parser.add_argument(
        "--ignore-html",
        action="append",
        default=["docs/overrides/*.html"],
        help="Generated-site HTML glob to skip while checking links. Can be supplied multiple times.",
    )
    args = parser.parse_args()

    site_dir = args.site_dir.resolve()
    if not site_dir.is_dir():
        print(f"Site directory does not exist: {site_dir}", file=sys.stderr)  # noqa: T201
        return 2

    errors = check_links(site_dir, check_anchors=args.check_anchors, ignored_html_patterns=args.ignore_html)
    if errors:
        print("\n--- Built Documentation Link Check: FAILED ---", file=sys.stderr)  # noqa: T201
        for error in errors:
            print(f"- {error}", file=sys.stderr)  # noqa: T201
        return 1

    print("Success: all internal links in the built documentation resolve.")  # noqa: T201
    return 0


if __name__ == "__main__":
    sys.exit(main())
