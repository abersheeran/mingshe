Example:

```
range(10) |> sum |> print
```

Compile to:

```python
print(sum(range(10)))
```

## Priority

The priority of `|>` is lower than `|` and higher than comparison operations (`in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==`).
