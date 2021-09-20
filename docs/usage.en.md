## As a script

Write the following code to `hello.she`, and then run `mingshe ./hello.she`.

```mingshe
"hello world" |> print
```

## As a module

Just like use a python module, you can use a MíngShé module.

```python
# lib.she
def digit_sum(s: str) -> int:
    return s |> map(int, ?) |> sum
```

```python
# main.py
from lib import digit_sum

print(digit_sum('123456'))
```

## Compile to python

Use `mingshe --compile ...` to compile to python.

## Run short code

Just try `mingshe -c "9 ** 106 |> print"`.

Also, you can use `mingshe --compile -c "9 ** 106 |> print"`.
