The unpack mapping syntax allows you to easily extract the value of the specified key in the mapping. If the expected key value does not exist, the variable is assigned to the default value of the `.get` method.

```
{ key } = one_dict
```

the equivalent code is:

```
key = (lambda **kwargs: kwargs.get('key'))(**one_dict)
```

## Grammar

```
{ name [, name] } = expression
```

## Trick

Any object that implements the `Mapping` type can be deconstructed using this syntax, such as `MultiDict` in Django.
