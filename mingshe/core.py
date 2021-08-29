import ast
import builtins
import token
from io import StringIO
from tokenize import TokenInfo, generate_tokens
from typing import Any, Iterable, List

from pegen.tokenizer import Tokenizer

from .parser import PythonParser


def tokenize(s: str) -> Iterable[TokenInfo]:
    for toknum, tokval, (srow, scol), (erow, ecol), linenum in generate_tokens(
        StringIO(s).readline
    ):
        yield TokenInfo(toknum, tokval, (srow, scol), (erow, ecol), linenum)


def merge_operators(tokens: Iterable[TokenInfo]) -> List[TokenInfo]:
    result = []
    for toknum, tokval, (srow, scol), (erow, ecol), linenum in tokens:
        if tokval == ">" and result[-1].string == "|":  # |>
            token_info = TokenInfo(token.OP, "|>", result[-1][2], (erow, ecol), linenum)
            del result[-1]
            result.append(token_info)
            continue
        elif tokval == "?":
            token_info = TokenInfo(token.OP, "?", (srow, scol), (erow, ecol), linenum)
            result.append(token_info)
            continue
        elif tokval == ">" and result[-1].string == "=":  # =>
            token_info = TokenInfo(token.OP, "=>", result[-1][2], (erow, ecol), linenum)
            del result[-1]
            result.append(token_info)
            continue

        result.append(TokenInfo(toknum, tokval, (srow, scol), (erow, ecol), linenum))
    return result


def compile(
    s: str,
    filename: str = "<unknown>",
    verbose_tokenizer: bool = False,
    verbose_parser: bool = False,
) -> ast.Module:
    tokengen = iter(merge_operators(tokenize(s)))
    tokenizer = Tokenizer(tokengen, verbose=verbose_tokenizer)
    parser = PythonParser(tokenizer, filename=filename, verbose=verbose_parser)
    try:
        return parser.parse("file")
    except SyntaxError as syntax_error:
        if not syntax_error.text:
            raise parser.make_syntax_error("unknown syntax error") from None
        else:
            raise


def exec(
    s: str,
    filename: str = "<unknown>",
    verbose_tokenizer: bool = False,
    verbose_parser: bool = False,
) -> Any:
    return builtins.exec(
        builtins.compile(
            compile(s, filename, verbose_tokenizer, verbose_parser), filename, "exec"
        )
    )
