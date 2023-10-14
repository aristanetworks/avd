# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from types import SimpleNamespace

OPERATORS = ["{", "}", "-", ","]
RANGE_OPERATORS = ["-", ","]
BRACES = ["{", "}"]
BRACES_OR_COMMA = ["{", "}", ","]


class TokenizerData(SimpleNamespace):
    string: str
    position: int
    length: int


def _number_token(data: TokenizerData) -> str:
    """
    Parses data.string gathering digits from the current position until the first non-digit character.
    Returns an string with the gathered digits.
    """
    start_position = data.position
    while data.position < data.length and data.string[data.position].isdigit():
        data.position += 1

    return data.string[start_position : data.position]


def _other_token(data: TokenizerData) -> str | None:
    """
    Parses data.string gathering non-digits and non-operators from the current position until the first digit or operator character.
    Returns a string with the gathered characters or None if the token is all whitespaces.
    """
    start_position = data.position
    while data.position < data.length and not data.string[data.position].isdigit() and data.string[data.position] not in BRACES_OR_COMMA:
        data.position += 1

    token = data.string[start_position : data.position]
    if token.isspace():
        return None

    return token


def _tokenizer(string: str) -> list:
    """
    Returns a list of tokens like
    [ "Ethernet", 123, "-", 234, ".", "{", 12, "-", 13, ",", 15, "}"]
    """
    # Keeping position in a dict so we can do inplace update.
    data = TokenizerData(string=string, position=0, length=len(string))
    tokens = []
    while data.position < data.length:
        if data.string[data.position].isdigit():
            tokens.append(_number_token(data))
        elif data.string[data.position] in OPERATORS:
            tokens.append(data.string[data.position])
            data.position += 1
        else:
            if (token := _other_token(data)) is not None:
                tokens.append(token)
    # raise Exception(tokens)
    return tokens


def _number_range(tokens: list) -> list[str]:
    """
    Return a list of numbers expanded from "-" and "," operators.
    "," is only expanded if inside braces.
    Popping consumed elements from the given tokens.
    """
    output = []
    in_braces = 0
    while tokens:
        token = tokens[0]
        if token.isdigit():
            output.append(int(tokens.pop(0)))
            continue

        if token == "-":
            if len(tokens) < 2:
                raise ValueError(f"Invalid range. Missing value following operator '{token}'.")
            if not tokens[1].isdigit():
                raise ValueError(f"Invalid range. Invalid value following operator '{token}'. The value must be numeric. Got '{tokens[1]}'.")

            # Remove the operator and pop the end value
            tokens.pop(0)
            start_value = output.pop()
            end_value = int(tokens.pop(0))
            if start_value > end_value:
                raise ValueError(f"Invalid range. Start value '{start_value}' is larger than end value '{end_value}'.")

            output.extend(range(start_value, end_value + 1))
            continue

        if token == "," and in_braces > 0:
            # Inside braces we expand comma operators with numeric values.
            if len(tokens) < 2:
                raise ValueError(f"Invalid range. Missing value following operator '{token}'.")
            if not tokens[1].isdigit():
                raise ValueError(f"Invalid range. Invalid value following operator '{token}'. The value must be numeric. Got '{tokens[1]}'.")

            # Since we already added the previous number, we can just pop the operator and continue.
            tokens.pop(0)
            continue

        if token == "{":
            in_braces += 1
            tokens.pop(0)
            continue

        if token == "}":
            in_braces -= 1
            tokens.pop(0)
            continue

        # The token was not a number, brace or a range operator, so we break out and return what we got.
        break

    if in_braces != 0:
        raise ValueError("Invalid range. Unmatched braces.")

    return output


def _tokens_until_comma(tokens: list) -> list:
    in_braces = 0
    tokens_until_comma = []
    while tokens:
        token = tokens[0]
        if in_braces == 0 and token == ",":
            break
        if token == "{":
            in_braces += 1
        elif token == "}":
            in_braces -= 1
        tokens_until_comma.append(tokens.pop(0))

    if in_braces != 0:
        raise ValueError("Invalid range. Unmatched braces")

    return tokens_until_comma


def _parser(tokens: list, prefix: str = "") -> list:
    if not tokens:
        if prefix:
            return [prefix]
        return []
    items = []
    while tokens:
        token = tokens[0]
        if token.isdigit() or token in BRACES:
            numbers = _number_range(tokens)
            # _range pops the numbers, braces and range operators from tokens so it is now a shorter list we recurse over.

            # Extend items up to the first comma (outside of braces).
            # _tokens_until_comma will pop the items from the original list.
            tokens_until_comma = _tokens_until_comma(tokens)
            for number in numbers:
                items.extend(_parser(tokens_until_comma.copy(), f"{prefix}{number}"))
            continue

        if token == "-":
            raise ValueError(f"Invalid range. Missing value before operator '{token}'.")

        if token == ",":
            if not items:
                raise ValueError(f"Invalid range. Missing value before operator '{token}'.")
            if len(tokens) < 2:
                raise ValueError(f"Invalid range. Missing value following for operator '{token}'.")
            # Remove the comma operator and we can add items after the comma.
            tokens.pop(0)
            # Before we continue, check if we have a new prefix after the comma (non-numeric token)
            # and clear the prefix if so.
            if not (tokens[0].isdigit() or tokens[0] in BRACES):
                prefix = ""
            continue

        # Other token so we just add it to the prefix.
        prefix += tokens.pop(0)

    return items


def range_expand(input_ranges) -> list:
    if isinstance(input_ranges, str):
        input_ranges = [input_ranges]
    elif not isinstance(input_ranges, list):
        raise TypeError(f"range_expand only accepts a string or a list. Got {type(input_ranges)}.")

    output = []
    for input_range in input_ranges:
        if not isinstance(input_range, str):
            raise TypeError(f"range_expand only accepts input_range items as strings. Got {type(input_range)}.")
        # raise Exception(_parser(_tokenizer(input_range)))
        output.extend(_parser(_tokenizer(input_range)))

    return output
