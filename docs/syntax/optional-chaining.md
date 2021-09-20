Example:

```
a?.b
```

Compile to:

```python
None if a is None else a.b
```

Example:

```
a?[b]
```

Compile to:

```python
None if a is None else a[b]
```

Example:

```
a?.b()
```

Compile to:

```python
None if a is None else a.b()
```

## Examples in real world

```python
file = None
try:
    file = open(filepath)
    ...
finally:
    file?.close()
```
