Partial function operators allow you to quickly create a new function by binding some parameters. Compared with the standard library `functools.partial`, it is more flexible and powerful.

## Grammar

```
f(?, 2)

f(?, ?, 3, ?)

f(a, b=?)

f(*?, b=10)

f(name="Aber", **?)
```

!!! tip ""
     Each `?` means to add a positional parameter to the generated function.

## Trick

When you need to pass a sequence, but only want to pass a parameter using a pipe (`|>`), please use `*?`.

Try to see the difference between `("hello", "world") |> print(?)` and `("hello", "world") |> print(*?)`.
