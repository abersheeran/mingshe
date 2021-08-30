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
