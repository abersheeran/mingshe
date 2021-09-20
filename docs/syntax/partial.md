Example:

```
square = pow(?, 2)
```

Compile to:

```python
(lambda pow: lambda _0: pow(_0, 2))(pow)
```

## Keyword

```
f(a, b=?)
```

Complie to:

```python
(lambda _p_0, f: lambda _0: f(_p_0, b=_0))(a, f)
```

## Multiple arguments

Positional arguments:

```
f(1, *?)
```

Compile to:

```python
(lambda f: lambda _0: f(1, *_0))(f)
```

Keyword arguments:

```
f(a, **?)
```

Compile to:

```python
(lambda _p_0, f: lambda _0: f(_p_0, **_0))(a, f)
```
