#!/usr/bin/env mingshe

range(10) |> sum |> print
10 |> print

sq = lambda iterable: map(lambda x: x * 2, iterable) |> list

range(10) |> sq |> print
