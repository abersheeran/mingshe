# MíngShé

A better [Python](https://www.python.org/) superset language. Use [Pegen](https://github.com/we-like-parsers/pegen) to compile the code.

> “鲜山多金玉，无草木，鲜水出焉，而北流注于伊水。其中多鸣蛇，其状如蛇而四翼，其音如磬，见则其邑大旱”——《山海经》

- [Documentation](https://mingshe.aber.sh/)
    - [English](https://mingshe.aber.sh/en/)

## Install

```
pip install mingshe
```

## Usage

### As a script

Write the following code to `hello.she`, and then run `mingshe ./hello.she`.

```mingshe
"hello world" |> print
```

### As a module

Just like use a python module, you can use a mingshe module.

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

### Compile to python

Use `mingshe --compile ...` to compile to Python code, and it can be compiled to the specified Python version: `mingshe --compile --python 2.7 ...`.

## Change log

Read [releases](https://github.com/abersheeran/mingshe/releases) to see the change log.
