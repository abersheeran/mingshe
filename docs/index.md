鸣蛇是一个 Python 超集语言，它使用 [Pegen](https://github.com/we-like-parsers/pegen) 语法解析器，将代码编译到 Python AST 进行运行。

除去 Python 本身支持的语法外（目前同步到 3.10），鸣蛇支持如下语法：

- 管道：`arg |> func`
- 条件运算：`condition ? true_branch : false_branch`
- 偏函数：`square = pow(?, 2)`
- 空值合并：`obj ?? other`
- 可选链：`obj?.attr`、`obj?[key]`、`obj?.func()`

## 编辑器插件

Visual Studio Code：

  - [vscode-mingshe](https://marketplace.visualstudio.com/items?itemName=frostming.vscode-mingshe)

## 其他相关网站

- [源代码托管](https://github.com/abersheeran/mingshe)
- [用户论坛](https://github.com/abersheeran/mingshe/discussions)
