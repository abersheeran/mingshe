from pathlib import Path
from typing import Iterable, List

from parso.python.tokenize import OP, ERRORTOKEN, PythonToken
from parso.grammar import PythonGrammar, parse_version_string


def merge_operators(tokens: Iterable[PythonToken]) -> List[PythonToken]:
    result: List[PythonToken] = []
    for token in tokens:
        if token.string == ">" and result[-1].string == "|":  # pipe operator
            if result[-2].string == "|":  # ||>
                if result[-3].string == "|":  # |||>
                    l = -3
                else:
                    l = -2
            else:  # |>
                l = -1
            operator = "|" * abs(l) + ">"
            token_info = PythonToken(
                result[l].type, operator, result[l].start_pos, prefix=result[l].prefix
            )
            del result[l:]
            result.append(token_info)
        elif token.type == ERRORTOKEN and token.string == "?":
            result.append(PythonToken(token.type, "?", token.start_pos, token.prefix))
        else:
            result.append(token)
    print(result)
    return result


class MíngShéGrammar(PythonGrammar):
    def __init__(self):
        super().__init__(
            parse_version_string(),
            (Path(__file__).absolute().parent / "mingshe.gram").read_text(),
        )

    def _tokenize_lines(self, lines, **kwargs):
        return merge_operators(super()._tokenize_lines(lines, **kwargs))

    def _tokenize(self, code):
        return merge_operators(super()._tokenize(code))
