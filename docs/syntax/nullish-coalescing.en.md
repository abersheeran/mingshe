The null coalescing operator looks very similar to the `or` operation, but `a or b` is equivalent to `a if a else b`, and `a ?? b` is equivalent to `a if a is None else b`. The difference between the two is that `a ?? b` judges the value of `None`, while `a or b` judges all false values (such as: `""`, `False`, `0`, ` []`, `{}`, etc.).

## Grammar

```
a ?? b
```

## Priority

`??` has the same priority as `or`.

## Notice

The priority between `??` and `or` is undetermined, so it cannot be used directly in chain. When you want `??` and `or` to appear in the same expression, then you need to put parentheses around them, otherwise a syntax error will be thrown.

```
a or b ?? c # syntax error
(a or b) ?? c # correct
a or (b ?? c) # correct
```
