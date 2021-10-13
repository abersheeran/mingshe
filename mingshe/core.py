import ast
import logging
import time
import token
from io import StringIO
from tokenize import TokenInfo, generate_tokens
from typing import Iterable, List, Literal, Optional, Tuple, overload

from pegen.tokenizer import Tokenizer

from .parser import PythonParser

log = logging.getLogger(__name__)


def merge_operators(tokens: Iterable[TokenInfo]) -> List[TokenInfo]:
    result = []
    for toknum, tokval, (srow, scol), (erow, ecol), linenum in tokens:
        if tokval == ">" and result[-1].string == "|":  # |>
            token_info = TokenInfo(token.OP, "|>", result[-1][2], (erow, ecol), linenum)
            del result[-1]
            result.append(token_info)
            continue
        elif tokval == "?":
            if result[-1].string == "?":  # ??
                token_info = TokenInfo(token.OP, "??", result[-1][2], (erow, ecol), linenum)
                del result[-1]
                result.append(token_info)
                continue
            else:
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


@overload
def compile(
    source: str,
    filename: str = "<unknown>",
    symbol: Literal["file"] = "file",
    verbose_tokenizer: bool = False,
    verbose_parser: bool = False,
    py_version: Optional[Tuple[int, int]] = None,
) -> ast.Module:
    ...


@overload
def compile(
    source: str,
    filename: str = "<unknown>",
    symbol: Literal["eval"] = "eval",
    verbose_tokenizer: bool = False,
    verbose_parser: bool = False,
    py_version: Optional[Tuple[int, int]] = None,
) -> ast.Expression:
    ...


@overload
def compile(
    source: str,
    filename: str = "<unknown>",
    symbol: Literal["interactive"] = "interactive",
    verbose_tokenizer: bool = False,
    verbose_parser: bool = False,
    py_version: Optional[Tuple[int, int]] = None,
) -> ast.Interactive:
    ...


@overload
def compile(
    source: str,
    filename: str = "<unknown>",
    symbol: Literal["func_type"] = "func_type",
    verbose_tokenizer: bool = False,
    verbose_parser: bool = False,
    py_version: Optional[Tuple[int, int]] = None,
) -> ast.FunctionType:
    ...


@overload
def compile(
    source: str,
    filename: str = "<unknown>",
    symbol: Literal["fstring"] = "fstring",
    verbose_tokenizer: bool = False,
    verbose_parser: bool = False,
    py_version: Optional[Tuple[int, int]] = None,
) -> ast.Expr:
    ...


def compile(
    source,
    filename="<unknown>",
    symbol="file",
    verbose_tokenizer=False,
    verbose_parser=False,
    py_version=None,
):
    start_time = time.time_ns()
    token_list = merge_operators(generate_tokens(StringIO(source).readline))
    tokenizer = Tokenizer(iter(token_list), verbose=verbose_tokenizer)
    parser = PythonParser(
        tokenizer, filename=filename, verbose=verbose_parser, py_version=py_version
    )
    try:
        return parser.parse(symbol)
    except SyntaxError as syntax_error:
        if parser._exception is None and str(syntax_error) == "invalid syntax":
            raise parser.make_syntax_error("unknown syntax error") from None
        else:
            raise
    finally:
        end_time = time.time_ns()
        log.debug(f"Compile {filename} took {(end_time - start_time) / 1e6:.2f} ms")
