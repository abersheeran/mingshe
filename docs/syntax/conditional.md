在 [PEP308](https://www.python.org/dev/peps/pep-0308/) 中 Guido 最终为 Python 选择了 `if-else` 作为条件运算的语法。鸣蛇增加了更符合传统语言习惯的三元条件运算符，无论你是喜欢 Guido 的设计还是 C 的设计，在鸣蛇里你都可以使用。

## 语法

```
a ? b : c
```

## 优先级

`a ? b : c` 与 `b if a else c` 的优先级相同。
