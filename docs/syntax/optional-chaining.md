可选链操作符与原始操作符的区别仅在于 `obj` 为空值（`None`）时，可选链操作符会返回 `None`，而原始操作符会抛出异常。

当尝试访问可能不存在的对象属性时，可选链操作符将会使表达式更短、更简明。

## 语法

```
obj?.attr

obj?[key]

obj?.method()
```

## 真实代码的示例

```python
import socket

sock = None
try:
    sock = socket.create_connection(('www.python.org', 80))
    ...
finally:
    sock?.close()
```

## 参考

- https://peps.python.org/pep-0505/
