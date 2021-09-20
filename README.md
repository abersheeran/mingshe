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

Write some code in `main.she`, then run `mingshe ./main.she` to execute code.

```python
10 |> range |> map(pow(?, 2), ?) |> list |> print
```

### Compile to python

You can use `mingshe --compile ./main.she` to generate python file.

### As a module

You can directly import MíngShé script as a module, as long as the script name ends with `.she`.

Example:

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

## Change log

Read [releases](https://github.com/abersheeran/mingshe/releases) to see the change log.
