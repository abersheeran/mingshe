Example:

```
square = pow(?, 2)
```

Compile to:

```python
(lambda pow: lambda _0: pow(_0, 2))(pow)
```
