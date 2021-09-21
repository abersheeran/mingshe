The pipeline operator allows to chain calls to functions in an easy-to-read way. When multiple functions are chained, using the pipeline operator can improve the readability of the code. Essentially, the pipeline operator is syntactic sugar for single-argument function calls, which allows you to perform a call like this:

```
10 |> range |> list |> print
```

To write using traditional syntax, the equivalent code is:

```python
print(list(range(10)))
```

## Grammar

```
arg |> function
```

## Priority

The priority of `|>` is lower than `|`, higher than comparison operators (`in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==`).
