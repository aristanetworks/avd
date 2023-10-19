# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import deque
from itertools import takewhile
from types import SimpleNamespace
from typing import Type


class Token(SimpleNamespace):
    """Base class for tokens"""

    value: str

    def __str__(self):
        return self.value

    def __repr__(self):
        return f'{self.__class__.__name__}(value="{self.value}")'


class DynamicToken(Token):
    """Dynamic tokens contain must be set with one or more characters from the input data."""

    @classmethod
    def get_token(cls, value: str) -> DynamicToken:
        return cls(value="".join(takewhile(cls.is_token, value)))


class NumberToken(DynamicToken):
    """Token for contiguous digits"""

    @classmethod
    def is_token(cls, value: str) -> bool:
        return value and value[0].isdigit()

    def __int__(self):
        return int(self.value)


class StringToken(DynamicToken):
    """Token for something we don't expand like a prefix or a dot."""

    @classmethod
    def is_token(cls, value: str) -> bool:
        # We accept "-"" if it is in a string to accept things like
        return value and not value[0].isdigit() and value[0] not in [",", "{", "}"]


class OperatorToken(Token):
    """Operator tokens always have a preset value attribute."""

    @classmethod
    def get_token(cls, value: str) -> OperatorToken:
        return cls()

    @classmethod
    def is_token(cls, value: str) -> bool:
        return value.startswith(cls.value)


class OpenBraceOperator(OperatorToken):
    value = "{"


class CloseBraceOperator(OperatorToken):
    value = "}"


class CommaOperator(OperatorToken):
    """Comma outside of braces , { }"""

    value = ","


class CommaInBracesOperator(OperatorToken):
    """Comma inside of braces { , }"""

    value = ","


class HyphenOperator(OperatorToken):
    value = "-"


class TokenizerData(SimpleNamespace):
    """
    Namespace to parse tokenizer data between various functions
    making them in-place updatable.
    """

    string: str
    position: int
    length: int


def _get_token(data: TokenizerData, token_types: Type[Token] | tuple[Type[Token]]) -> Token | None:
    """
    Parses data.string gathering characters from the current position.
    For non-operators it consumes characters until the first character not matching the requested token type.
    For operators it consumes only characters matching the token.
    Returns the requested token type with the gathered characters.
    Advances data.position for consumed characters.
    """
    if not isinstance(token_types, tuple):
        token_types = (token_types,)

    for token_type in token_types:
        if not token_type.is_token(data.string[data.position :]):
            continue

        token = token_type.get_token(data.string[data.position :])
        data.position += len(token.value)

        if isinstance(token, StringToken) and token.value.isspace():
            # We got only spaces so we return None
            return None

        return token
    return None


def _tokenizer(string: str) -> deque[Token]:
    """
    Returns a deque of tokens found in the given string.
    Example:
    "Ethernet123-234.{12-13,15}" ->
        [
            StringToken(value="Ethernet"),
            NumberToken(value="123"),
            HyphenOperator(),
            NumberToken(value="234"),
            StringToken(value="."),
            OpenBraceOperator(),
            NumberToken(value="12"),
            HyphenOperator(),
            NumberToken(value="13"),
            CommaInBracesOperator(),
            NumberToken(value="15"),
            CloseBraceOperator(),
        ]
    """
    # Keeping position in a namespace so we can do in-place update.
    data = TokenizerData(string=string, position=0, length=len(string))
    tokens = deque()
    in_braces = 0
    while data.position < data.length:
        # The order below is important since we have commas inside or outside of braces.
        if (token := _get_token(data, OpenBraceOperator)) is not None:
            in_braces += 1
        elif (token := _get_token(data, CloseBraceOperator)) is not None:
            in_braces -= 1
        elif in_braces != 0 and (token := _get_token(data, CommaInBracesOperator)) is not None:
            pass
        else:
            if (token := _get_token(data, (NumberToken, HyphenOperator, CommaOperator, StringToken))) is None:
                continue

        tokens.append(token)

    if in_braces != 0:
        raise ValueError("Invalid range. Unmatched braces.")
    return tokens


def _number_range(tokens: deque) -> deque[str]:
    """
    Return a deque of numbers expanded from "-" and "," operators.
    "," is only expanded if inside braces.

    Consumes tokens until first token which is not numeric, brace, "-" or "," inside braces.
    Popping consumed elements from the given tokens.
    """
    output = deque()
    while tokens:
        token = tokens[0]
        if isinstance(token, NumberToken):
            output.append(int(tokens.popleft()))
            continue

        if isinstance(token, HyphenOperator):
            if len(tokens) < 2:
                raise ValueError(f"Invalid range. Missing numeric value following operator '{token}'.")
            if not isinstance(tokens[1], NumberToken):
                raise ValueError(f"Invalid range. Invalid value following operator '{token}'. The value must be numeric. Got '{tokens[1]}'.")

            # Remove the operator and pop the end value
            tokens.popleft()
            start_value = output.pop()
            end_value = int(tokens.popleft())
            if start_value > end_value:
                raise ValueError(f"Invalid range. Start value '{start_value}' is larger than end value '{end_value}'.")

            output.extend(range(start_value, end_value + 1))
            continue

        if isinstance(token, CommaInBracesOperator):
            # Inside braces we expand comma operators with numeric values.
            if len(tokens) < 2:
                raise ValueError(f"Invalid range. Missing numeric value following operator '{token}'.")
            if not isinstance(tokens[1], NumberToken):
                raise ValueError(f"Invalid range. Invalid value following operator '{token}'. The value must be numeric. Got '{tokens[1]}'.")

            # Since we already added the previous number, we can just pop the operator and continue.
            tokens.popleft()
            continue

        if isinstance(token, (OpenBraceOperator, CloseBraceOperator)):
            # Nothing to do here.
            tokens.popleft()
            continue

        # The token was not a number, brace or a range operator, so we break out and return.
        break

    return output


def _tokens_until_comma(tokens: deque) -> deque[str]:
    """
    Returns a subset if the given deque starting from index 0
    and ending before the first found "," outside of braces.

    Popping returned tokens from the given tokens.
    """
    # return list(popwhile(lambda item: not isinstance(item, CommaOperator), tokens))
    tokens_until_comma = deque()
    while tokens and not isinstance(tokens[0], CommaOperator):
        tokens_until_comma.append(tokens.popleft())

    return tokens_until_comma


def _parser(tokens: deque, prefix: str = "") -> list[str]:
    """
    Return list of strings expanded from the given tokens.

    The fuction is called recursively to expand multiple ranges in the right order:
    Tokens ["Ethernet", "11", "-", "12", "/", "1" - "2"]
    becomes ["Ethernet11/1" "Ethernet11/2", "Ethernet12/1", "Ethernet12/2"]
    so the first "-" is resolved into 11, 12 which are then looped over to call the function
    recursively to expand deeper into the tokens.
    """
    if not tokens:
        if prefix:
            return [prefix]
        return []
    items = []
    while tokens:
        token = tokens[0]

        if isinstance(token, (NumberToken, OpenBraceOperator)):
            # Extend items up to the first comma (outside of braces).

            # _number_range pops the numbers, braces and range operators from tokens so it is now a shorter list we recurse over.
            numbers = _number_range(tokens)

            # _tokens_until_comma will pop the items from the original list.
            tokens_until_comma = _tokens_until_comma(tokens)

            for number in numbers:
                # Since _parser will pop items from the given tokens, we have to provide an individual copy for each loop
                # so each of them will expand all the following tokens.
                items.extend(_parser(tokens_until_comma.copy(), f"{prefix}{number}"))
            continue

        if isinstance(token, HyphenOperator):
            # "-" alone is only supported between numeric operators.
            raise ValueError(f"Invalid range. Missing numeric value before operator '{token}'.")

        if isinstance(token, CommaOperator):
            if not items:
                raise ValueError(f"Invalid range. Missing numeric value before operator '{token}'.")
            if len(tokens) < 2:
                raise ValueError(f"Invalid range. Missing numeric value after operator '{token}'.")
            # Remove the comma operator and we can add items after the comma.
            tokens.popleft()
            # Before we continue, check if we have a new prefix after the comma (non-numeric token)
            # and clear the prefix if so.
            if not isinstance(tokens[0], (NumberToken, OpenBraceOperator)):
                prefix = ""
            continue

        # Other token so we just add it to the prefix.
        prefix += str(tokens.popleft())

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
