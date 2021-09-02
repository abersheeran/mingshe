# MíngShé

A better [Python](https://www.python.org/) superset language.

> “鲜山多金玉，无草木，鲜水出焉，而北流注于伊水。其中多鸣蛇，其状如蛇而四翼，其音如磬，见则其邑大旱”——《山海经》

## Install

```
pip install mingshe
```

## Example

Write some code in `main.she`, then run `mingshe ./main.she` to execute code.

```python
import time

start_time = time.time_ns()
for _ in range(10 ** 6):
    10 |> range |> map(pow(?, 2), ?) |> list
end_time = time.time_ns()
print("Time:", (end_time - start_time) / 10 ** 6, "ms")
```

You can also use `mingshe --compile ./main.she` to generate python file.

## Extended syntax

### Pipe

Example:

```
range(10) |> sum |> print
```

Compile to:

```python
print(sum(range(10)))
```

### Conditional

Example:

```
a ? b : c
```

Compile to:

```python
b if a else c
```

### Partial

Example:

```
square = pow(?, 2)
```

Compile to:

```python
(lambda pow: lambda _0, /: pow(_0, 2))(pow)
```
