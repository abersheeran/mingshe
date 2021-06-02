import ast
from typing import Union

from parso.python.tree import Operator, PythonNode, PythonLeaf

from .grammar import MíngShéGrammar


def swap_prefix(
    left: Union[PythonNode, PythonLeaf], right: Union[PythonNode, PythonLeaf]
) -> None:
    if isinstance(left, PythonLeaf):
        if isinstance(right, PythonLeaf):
            left.prefix, right.prefix = right.prefix, left.prefix
        else:
            return swap_prefix(left, right.children[0])
    else:
        if isinstance(right, PythonLeaf):
            return swap_prefix(left.children[0], right)
        else:
            return swap_prefix(left.children[0], right.children[0])


class ParsoNodeTransformer:
    def transform(self, point: PythonNode) -> None:
        for node in point.children:
            if isinstance(node, PythonNode):
                self.visit_node(node)
                self.transform(node)
            else:
                self.visit_leaf(node)

    def visit_leaf(self, leaf: PythonLeaf):
        pass

    def visit_node(self, node: PythonNode):
        pass


class PipeTransformer(ParsoNodeTransformer):
    def visit_node(self, node: PythonNode):
        i = 0
        while i < len(node.children):
            if isinstance(node.children[i], Operator) and node.children[i].value in (
                "|>",
                "||>",
                "|||>",
            ):
                func_leaf = node.children[i + 1]
                param_leaf = node.children[i - 1]
                swap_prefix(func_leaf, param_leaf)
                if node.children[i].value == "|>":
                    node.children[i - 1 : i + 2] = [
                        PythonNode(
                            "pipe_call",
                            [
                                func_leaf,
                                Operator("(", func_leaf.start_pos),
                                param_leaf,
                                Operator(")", func_leaf.start_pos),
                            ],
                        ),
                    ]
                elif node.children[i].value == "||>":
                    node.children[i - 1 : i + 2] = [
                        PythonNode(
                            "pipe_call",
                            [
                                func_leaf,
                                Operator("(", func_leaf.start_pos),
                                PythonNode(
                                    "",
                                    [
                                        Operator("*", func_leaf.start_pos),
                                        Operator("(", func_leaf.start_pos),
                                        param_leaf,
                                        Operator(")", func_leaf.start_pos),
                                    ],
                                ),
                                Operator(")", func_leaf.start_pos),
                            ],
                        ),
                    ]
                elif node.children[i].value == "|||>":
                    node.children[i - 1 : i + 2] = [
                        PythonNode(
                            "pipe_call",
                            [
                                func_leaf,
                                Operator("(", func_leaf.start_pos),
                                PythonNode(
                                    "",
                                    [
                                        Operator("**", func_leaf.start_pos),
                                        Operator("(", func_leaf.start_pos),
                                        param_leaf,
                                        Operator(")", func_leaf.start_pos),
                                    ],
                                ),
                                Operator(")", func_leaf.start_pos),
                            ],
                        ),
                    ]
                else:
                    pass

                i -= 1
            else:
                i += 1


def compile(code: str) -> ast.AST:
    grammar = MíngShéGrammar()
    module = grammar.parse(code)

    v = PipeTransformer()
    v.transform(module)

    return ast.parse(module.get_code())
