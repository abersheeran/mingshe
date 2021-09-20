MíngShé is a Python superset language. It uses the [Pegen](https://github.com/we-like-parsers/pegen) syntax parser to compile the code to Python AST for execution.

In addition to the syntax supported by Python itself (currently synchronized to 3.10), MíngShé supports the following syntax:

- Pipeline: `arg |> func`
- Conditional: `condition? True_branch: false_branch`
- Partial function: `square = pow(?, 2)`
- Null merge: `obj ?? other`
- Optional chain: `obj?.attr`, `obj?[key]`, `obj?.func()`

## Editor plugins

Visual Studio Code:

  - [vscode-mingshe](https://marketplace.visualstudio.com/items?itemName=frostming.vscode-mingshe)

## Other related websites

- [Source Code](https://github.com/abersheeran/mingshe)
- [User Forum](https://github.com/abersheeran/mingshe/discussions)
