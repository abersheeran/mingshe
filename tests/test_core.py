import ast
import inspect

import pytest

import mingshe.core


@pytest.mark.parametrize(
    "raw,result",
    [
        (
            "1 |> print",
            "print(1)",
        ),
        (
            "(1, 11) |> range(*)",
            "range((1, 11))",
        ),
        (
            "[1] |> max",
            "max([1])",
        ),
        (
            "{1} |> max",
            "max({1})",
        ),
        (
            "{'a': 1} |> max",
            "max({'a': 1})",
        ),
        (
            "range(10) |> sum |> print",
            "print(sum(range(10)))",
        ),
        (
            """
            "hello" |> print
            "world" |> print
            """,
            """
            print("hello")
            print("world")
            """,
        ),
        (
            "10 |> partial(print, 'num:')",
            "partial(print, 'num:')(10)",
        ),
    ],
)
def test_compile(raw, result):
    assert ast.unparse(
        ast.parse(mingshe.core.compile(inspect.cleandoc(raw)))
    ) == ast.unparse(ast.parse(inspect.cleandoc(result)))
