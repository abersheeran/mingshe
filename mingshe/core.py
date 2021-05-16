import token
from io import StringIO
from tokenize import TokenInfo, generate_tokens, untokenize
from typing import Iterable, List


def tokenize(s: str) -> Iterable[TokenInfo]:
    for toknum, tokval, (srow, scol), (erow, ecol), linenum in generate_tokens(
        StringIO(s).readline
    ):
        yield TokenInfo(toknum, tokval, (srow, scol), (erow, ecol), linenum)


def merge_operators(tokens: Iterable[TokenInfo]) -> List[TokenInfo]:
    result = []
    for toknum, tokval, (srow, scol), (erow, ecol), linenum in tokens:
        if tokval == ">" and result[-1].string == "|":  # pipe operator
            if result[-2][1] == "|":  # ||>
                token_info = TokenInfo(
                    token.OP, "||>", result[-2][2], (erow, ecol), linenum
                )
                del result[-2:]
            else:  # |>
                token_info = TokenInfo(
                    token.OP, "|>", result[-1][2], (erow, ecol), linenum
                )
                del result[-1]
            result.append(token_info)
            continue
        result.append(TokenInfo(toknum, tokval, (srow, scol), (erow, ecol), linenum))
    return result


class PipeOperator:
    tokvals = (
        "",
        "\n",
        ":=",
        "lambda",
        "if",
        "else",
        "or",
        "and",
        "not",
        "is",
        "in",
        "<",
        "<=",
        ">",
        ">=",
        "!=",
        "==",
        "||>",
        "|>",
    )

    @classmethod
    def rfind_split(cls, li: List[TokenInfo]) -> int:
        for i in reversed(range(len(li))):
            if li[i][1] in cls.tokvals:
                return i + 1
        return 0

    @classmethod
    def lfind_split(cls, li: List[TokenInfo]) -> int:
        for i in range(len(li)):
            if li[i][1] in cls.tokvals:
                return i
        return -1


def compile(s: str) -> str:
    result = []
    tokens = merge_operators(tokenize(s))
    i = 0
    while i < len(tokens):
        toknum, tokval, *_ = tokens[i]

        if tokval in ("||>", "|>"):
            left_i = PipeOperator.rfind_split(result)
            right_i = PipeOperator.lfind_split(tokens[i + 1 :])
            if tokval == "||>":
                left_expression = result[left_i:]
                if len(left_expression) <= 1 or left_expression[0][1] in (
                    "{",
                    "[",
                    "(",
                ):
                    left_expression = [(token.OP, "*"), *left_expression]
                else:
                    left_expression = [
                        (token.OP, "*"),
                        (token.OP, "("),
                        *left_expression,
                        (token.OP, ")"),
                    ]
            else:
                left_expression = result[left_i:]
            right_expression = [
                (toknum, tokval)
                for toknum, tokval, *_ in tokens[i + 1 : i + 1 + right_i]
            ]
            expression = []
            if len(right_expression) <= 1 or right_expression[0][1] == "(":
                expression += right_expression
            else:
                expression += [(token.OP, "("), *right_expression, (token.OP, ")")]
            expression += [(token.OP, "("), *left_expression, (token.OP, ")")]

            del result[left_i:]
            result.extend(expression)
            i = i + 1 + right_i
            continue

        result.append((toknum, tokval))
        i += 1
    return untokenize(result)
