In [PEP308](https://www.python.org/dev/peps/pep-0308/) Guido finally chose `if-else` as the syntax for conditional operations for Python. MíngShé has added a ternary conditional operator that is more in line with traditional language habits. Whether you like the design of Guido or the design of C, you always can use it in MíngShé.

## Grammar

```
a ? b : c
```

## Priority

`a ? b : c` has the same priority as `b if a else c`.
