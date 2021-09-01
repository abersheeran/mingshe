# MíngShé

A better [Python](https://www.python.org/) superset language.

## Install

```
pip install mingshe
```

## Pipe

Example:

```
range(10) |> sum |> print
```

Compile to:

```python
print(sum(range(10)))
```

## Conditional

Example:

```
a ? b : c
```

Compile to:

```python
b if a else c
```

## Partial

Example:

```
square = pow(?, 2)
```

Compile to:

```python
(lambda _p_0, /, pow: (lambda _0, /: pow(_0, _p_0)))(2, pow)
```
