from pyparsing import (
    Word,
    alphas,
    alphanums,
    Forward,
    delimitedList,
    Group,
    Combine,
    Keyword,
    Suppress,
    Regex,
    quotedString,
    Literal,
    oneOf,
    replaceWith,
    Optional,
)

lparen, rparen, lbrack, rbrack, lbrace, rbrace, colon, comma = map(Suppress, "()[]{}:,")

# 定义字面量
integer_literal = (
    Regex(r"[+-]?0x[\da-f]+").setName("hex-number")
    | Regex(r"[+-]?0o[0-7]+").setName("octal-number")
    | Regex(r"[+-]?0b[01]+").setName("binary-number")
    | Regex(r"[+-]?\d+").setName("integer")
)

float_literal = Regex(r"[+-]?\d+\.\d*([Ee][+-]?\d+)?").setName("float-number")

string_literal = Combine(
    (
        Optional(Literal("rf") | Literal("fr") | Literal("r") | Literal("f"))
        + quotedString.copy()
    ).setName("string")
) | Combine(Literal("u") + quotedString.copy()).setName("unicode-string")

bytes_literal = Combine(Literal("b") + quotedString.copy())

bool_literal = oneOf("True False", asKeyword=True).setParseAction(
    lambda tokens: tokens[0] == "True"
)

none_literal = Keyword("None").setParseAction(replaceWith(None))

ellipsis_literal = Keyword("...").setParseAction(replaceWith(...))

tuple_literal = Forward()

list_literal = Forward()

set_literal = Forward()

dict_literal = Forward()

literals = (
    none_literal
    | ellipsis_literal
    | bool_literal
    | float_literal
    | integer_literal
    | string_literal
    | bytes_literal
    | list_literal
    | tuple_literal
    | set_literal
    | dict_literal
)
# 定义字面量结束

identifier = Word(alphas + "_", alphanums + "_")

expr = Forward()

func_call = Forward()

expr <<= identifier | literals | func_call

tuple_literal <<= lparen + Optional(delimitedList(expr)) + Optional(comma) + rparen

list_literal <<= lbrack + Optional(delimitedList(expr) + Optional(comma)) + rbrack

set_literal <<= lbrace + Optional(delimitedList(expr) + Optional(comma)) + rbrace

dict_entry = Group(expr + colon + expr)
dict_literal <<= lbrace + Optional(delimitedList(dict_entry) + Optional(comma)) + rbrace

func_call << identifier + lparen + delimitedList(
    Group(expr | (identifier + "=" + expr))
) + Optional(comma) + rparen
