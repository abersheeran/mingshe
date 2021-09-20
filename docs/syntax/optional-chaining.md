Example:

```
a?.b
```

Compile to:

```python
a if a is None else a.b
```

Example:

```
a?[b]
```

Compile to:

```python
a if a is None else a[b]
```

Example:

```
a?.b()
```

Compile to:

```python
a if a is None else a.b()
```
