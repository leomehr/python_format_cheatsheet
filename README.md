# Python Formatting Cheatsheet

Python has surprisingly expressive string formatting options. It's handy to know
these whenever you're reading/writing lots of string data -- especially if
you're building internal/devtools and care about how things looks in the
terminal.

Simplified, annotated spec from [the docs](https://docs.python.org/3.11/library/string.html#format-specification-mini-language):
```
format_spec     ::=  [[fill]align][sign][width][grouping_option]["." precision][type]
fill            ::=  <any character>
  (the padding character to use)

align           ::=  "<" | ">" | "=" | "^"
  (left, right, pad around +/- for nums, center)

sign            ::=  "+" | "-" | " "
  (when to display sign for numbers)

width           ::=  digit+
  (min width to pad to)

grouping_option ::=  "_" | ","
  (grouping thousands in numbers e.g. 2000 -> 2,000 or 2_000)

precision       ::=  digit+
  (how many floating point digits)

type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
  (d = decimal, f = float, % = as percentage, etc.)
```

Some highlights, see `examples.py` for more:
```python
print(f'add commas: {1234567:,}')
# 1,234,567

print(f'show percent: {0.915:.1%}')
# 91.5%

x = 'pad right'
print(f'|{x:>15}|')
# |      pad right|

x = 'center'
print(f'{x:_^12}')
# ___center___
```

```
       0    1    2    3
   /----------------------\
0  | \   /\   /\   /\   / |
1  |  \ /  \ /  \ /  \ /  |
2  |   /    /    /    /   |
3  |  / \  / \  / \  / \  |
4  | /   \/   \/   \/   \ |
5  | \   /\   /\   /\   / |
6  |  \ /  \ /  \ /  \ /  |
7  |   /    /    /    /   |
   \----------------------/
```