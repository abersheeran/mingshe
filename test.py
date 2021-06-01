from typing import Tuple
from parso.tree import Node, NodeOrLeaf
from mingshe.grammar import MíngShéGrammar


grammar = MíngShéGrammar()

code = """
1 |> print

range(10) |> sum |> print

1 |> (lambda x: x**2)

def t():
    "call t" |> print
"""

module = grammar.parse(code)

from parso.python.tree import Module, Operator, PythonNode, PythonLeaf


def swap_prefix(left: NodeOrLeaf, right: NodeOrLeaf) -> Tuple[NodeOrLeaf, NodeOrLeaf]:
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


class ParsoNodeVisitor:
    def __init__(self, root: Module) -> None:
        self.root = root

    def visit(self, point=None) -> None:
        if point is None:
            point = self.root

        if not hasattr(point, "children"):
            return
        for node in point.children:
            if isinstance(node, PythonNode):
                self.visit_node(node)
            else:
                self.visit_leaf(node)
            self.visit(node)

    def visit_leaf(self, leaf: PythonLeaf):
        pass

    def visit_node(self, node: PythonNode):
        i = 0
        while i < len(node.children):
            if (
                isinstance(node.children[i], Operator)
                and node.children[i].value == "|>"
            ):
                func_leaf = node.children[i + 1]
                param_leaf = node.children[i - 1]
                swap_prefix(func_leaf, param_leaf)
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
                i -= 1
            else:
                i += 1


v = ParsoNodeVisitor(module)
v.visit()

import ast
import astunparse

print(code)
print(astunparse.unparse(ast.parse(v.root.get_code())))
