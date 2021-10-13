The difference between the optional chain operator and the primitive operator is only that when `obj` is a null value (`None`), the optional chain operator will return `None`, and the primitive operator will throw an exception.

When trying to access object properties that may not exist, the optional chain operator will make the expression shorter and more concise.

## Grammar

```
obj?.attr

obj?[key]

obj?.method()
```

## Examples of real code

```python
import socket

sock = None
try:
     sock = socket.create_connection(('www.python.org', 80))
     ...
finally:
     sock?.close()
```
