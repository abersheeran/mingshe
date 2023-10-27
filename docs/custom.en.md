MíngShé is not only a superset of the Python language but also a template for creating programming languages that compile to Python.

## Create a Repository

Open the [MíngShé GitHub repository](https://github.com/abersheeran/MíngShé) on your computer and click the "Use this template" button on the interface.

![Use this template](./img/use-this-template.png)

## Modify the Syntax and Generate the Parsing File

MíngShé uses [Pegen](https://github.com/we-like-parsers/pegen) to parse files, and the syntax description is located in the `MíngShé.gram` file in the project's root directory. After making the necessary modifications, execute `python script\generate.py` to generate a pure Python compiler for the syntax you described.

### Parsing the Syntax File

The syntax file is divided into two main sections: the code that will be inserted at the beginning of the generated parser file, and the grammar rules.

In the header code, you can encapsulate some compilation processes for convenience when writing grammar rules, such as `make_partial_function`, `make_nullish_coalescing`, `make_optional_chaining`, etc.

### Grammar Rules

!!! tip "Left Recursion"

    Pegen can handle left-recursive grammars, so you don't need to manually eliminate left recursion while writing the grammar rules.

#### `# comment`

Python-style comments.

#### `e1 e2`

Matches `e1` and then `e2`.

```
rule_name: first_rule second_rule
```

#### `e1 | e2`

Matches either `e1` or `e2`.

For formatting purposes, the first alternative can also appear on the line after the rule name. In this case, the `|` must be used before the first alternative, as shown below:

```
rule_name[return_type]:
    | first_alt
    | second_alt
```

#### `( e )`

Matches `e`.

```
rule_name: (e)
```

A slightly more complex and useful example: using grouping parentheses with repetition operators:

```
rule_name: (e1 e2)*
```

#### `[ e ]` or `e?`

Optionally matches `e`.

```
rule_name: [e]
```

A more useful example: defining trailing commas as optional:

```
rule_name: e (',' e)* [',']
```

#### `e*`

Matches `e` zero or more times.

```
rule_name: (e1 e2)*
```

#### `e+`

Matches `e` one or more times.

```
rule_name: (e1 e2)+
```

#### `s.e+`

Matches one or more `e` separated by `s`. The generated parse tree does not include the separators, otherwise it is the same as `(e (s e)*)`.

```
rule_name: ','.e+
```

#### `&e`

Attempts to match `e` without consuming any input.

#### `!e`

Attempts to match anything except `e` without consuming any input.

A Python syntax example: `primary` consists of an atom and is not allowed to be followed by `.` or `(` or `[`:

```
primary: atom !'.' !'(' !'['
```

#### `~`

Forces the current matching rule to continue even if subsequent matches fail.

In the following example, if a left parenthesis is successfully matched, no other alternatives will be considered, even if `some_rule` or `')'` fails to parse.

```
rule_name: '(' ~ some_rule ')' | some_alt
```

#### Assignments within Rules

Within a rule, you can name partial matches for use in generating the AST.

```
rule_name[return_type]: '(' a=some_other_rule ')' { a }
```

#### Actions after Matching

An action can be any valid Python statement, and its return value will be used as the value of the corresponding node.

```
rule_name[return_type]:
    | first_alt1 first_alt2 { first_action }
    | second_alt1 second_alt2 { second_action }
```

You can return an AST object, e.g., `{ ast.Add() }`, or call a function, e.g., `{ self.make_partial_function() }`.

!!! tip "LOCATIONS"

    `LOCATIONS` is a special variable that is equivalent to passing a dictionary as a keyword argument, containing the current location information.

## Final Step: The Renaming Magic

Use a modern editor to search for `MíngShé` throughout the project and replace it with the name you prefer. Now you have a user-friendly superset language that can exist as a Python module.

## How to Use Your Own Language

Use it just like you would use MíngShé.
