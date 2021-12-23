字典解构赋值语法允许你便捷的摘取字典中指定的键的值，若期望取出的键值不存在，则变量被赋值为 `.get` 方法的默认值。

```
{ key } = one_dict
```

其等价于：

```
key = (lambda **kwargs: kwargs.get('key'))(**one_dict)
```

## 语法

```
{ name [, name] } = expression
```

## 使用技巧

任何实现了 `Mapping` 类型的对象都可以使用这种语法进行解构，例如 Django 里的 `MultiDict`。
