鸣蛇不仅仅是一个 Python 超集语言，也是编写一个能编译到 Python 的编程语言的模板。

## 创建仓库

使用电脑打开[鸣蛇的 GitHub 地址](https://github.com/abersheeran/mingshe)，点击界面上的 `Use this template` 按钮。

![Use this template](./img/use-this-template.png)

## 修改语法并生成解析文件

鸣蛇使用 [Pegen](https://github.com/we-like-parsers/pegen) 对文件进行解析，语法描述都在项目根目录下的 `mingshe.gram` 里。修改完成后执行 `python script\generate.py` 即可为你所描述的语法生成一个纯 Python 编译器。

### 语法文件剖析

整个语法文件分为两大块，一个是插入最终生成的解析器文件头部的代码，一个是语法规则。

在头部代码里，我们可以自行封装一些编译过程，例如 `make_partial_function`、`make_nullish_coalescing`、`make_optional_chaining` 等，这是为了后续编写语法规则时更加方便地使用这些过程。

### 语法规则

!!! tip "左递归"

    Pegen 可以解析左递归语法，所以你在编写语法规则的时候不必自己在脑子里解决左递归。

#### `# comment`

Python 风格的注释。

#### `e1 e2`

匹配 e1 然后匹配 e2。

```
rule_name: first_rule second_rule
```

#### `e1 | e2`

匹配 e1 或 e2。

出于格式化目的，第一个选项也可以出现在规则名称之后的行上。 在这种情况下，`|` 必须在第一个选项之前使用，如下所示：

```
rule_name[return_type]:
    | first_alt
    | second_alt
```

#### `( e )`

匹配 e。

```
rule_name: (e)
```

一个稍微复杂和有用的示例：将分组运算符与重复运算符一起使用：

```
rule_name: (e1 e2)*
```

#### `[ e ] or e?`

非必需地匹配 e。

```
rule_name: [e]
```

一个更有用的例子：定义尾随逗号是可选的：

```
rule_name: e (',' e)* [',']
```

#### `e*`

匹配零次或多次出现的 e。

```
rule_name: (e1 e2)*
```

#### `e+`

匹配一次或多次出现的 e。

```
rule_name: (e1 e2)+
```

#### `s.e+`

匹配一个或多个 e，以 s 分隔。生成的解析树不包含分隔符，在其他方面与``(e (s e)*)``相同。

```
rule_name: ','.e+
```

#### `&e`

尝试匹配 e 且不消耗任何输入。

#### `!e`

尝试匹配非 e 且不消耗任何输入。

取自 Python 语法的一个示例：`primary` 由一个原子组成，其后不允许跟随 `.` 或 `(` 或 `[`：

```
primary: atom !'.' !'(' !'['
```

#### `~`

强制继续当前的匹配规则，即使它后续匹配失败。

在如下示例中，如果成功匹配左括号，则不会考虑其他替代方案，即使 `some_rule` 或 `')'` 无法解析。

```
rule_name: '(' ~ some_rule ')' | some_alt
```

#### 规则内赋值

在一个规则中，你可以对部分匹配进行命名，以便在生成 AST 时使用。

```
rule_name[return_type]: '(' a=some_other_rule ')' { a }
```

#### 匹配后执行动作

动作必须是任何有效的 Python 语句，且它的返回值会作为该节点的值。

```
rule_name[return_type]:
    | first_alt1 first_alt2 { first_action }
    | second_alt1 second_alt2 { second_action }
```

你可以返回一个 ast 对象，例如 `{ ast.Add() }`；也可以调用一个函数，例如 `{ self.make_partial_function() }`。

!!! tip "LOCATIONS"

    `LOCATIONS` 是一个特殊的变量，它等价于以关键词参数的形式传入一个字典，其中包含了当前的位置信息。

## 最后一步：改名大法

使用一个现代编辑器在整个项目里搜索 `mingshe`，修改成你喜欢的名称。一个简单易用的、可以作为 Python 模块存在的超集语言就做好了。

## 如何使用你自己的语言

就像使用鸣蛇一样使用它。
