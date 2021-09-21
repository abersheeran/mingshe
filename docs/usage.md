## 作为一个直接执行的脚本

把下面的代码写入 `hello.she` 文件，然后运行 `mingshe ./hello.she`。

```mingshe
"hello world" |> print
```

## 作为一个模块

就像导入一个 Python 模块一样，你也可以直接使用 import 命令导入一个鸣蛇模块。

```python
# lib.she
def digit_sum(s: str) -> int:
    return s |> map(int, ?) |> sum
```

```python
# main.py
from lib import digit_sum

print(digit_sum('123456'))
```

## 编译到 Python

使用 `mingshe --compile ...` 编译到 Python 代码，并且可以编译到指定的 Python 版本：`mingshe --compile --python 2.7 ...`。

## 运行小段代码

例如 `mingshe -c "9 ** 106 |> print"`。

你也可以直接使用 `mingshe --compile -c "9 ** 106 |> print"` 来看看编译结果。
