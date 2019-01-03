# My notes

## Recommended environment
- text editor
- ipython shell
- jupyter notebooks

## IPython and Jupyter "Now I know"
- `%run 'filename.py'` executes the script and loads assets into memory in the shell session
- IPython pretty prints data by default
- Run jupyter with `jupyter notebook`
- `shift + Enter` evaluates a line (or block) of code
- tab-autocomplete is super useful and grows with new values and functions in scope (like a good editor)
- `%run -i` instead of `%run` allows the script acces to variables already defined in the interactive ipython namespace.
- `%load` imports a script
- `%paste` pastes text from the clipboard
- `%cpaste` provides a prompt for pasting code
- `%timeit`  
- `%pwd` to print working directory

- get help on magic functions by doing `%debug?` or `%run?`

## Making random data
```python
import numpy as np

data = {i : np.random.randn() for i in range(7)}
```

## CLI Keyboard shortcuts that work in ipython and jupyter
- ctrl+l to clear screen
- ctrl +b to move cursor back one character
- ctrl + f to move cursor forward one character
- ctrl + u discard text from cursor to beginning of line
- ctrl + k discard text from cursor until end of current line
- ctrl + e move cursor to end of line
- ctrl + a move cursor to beginning of line

## Magic commands
- `%quickred`
- `%magic`
- `%debug`
- `%hist`
- `%pdb`
- `%paste`
- `%cpaste`
- `%reset`
- `%page OBJECT`
- `%run script.py`
- `%prun statement`
- `%time statement`
- `%tieit statement`
- `%who`
- `%who_ls` 
- `%whos`
- `%matplotlib` or `%matplotlib inline` for jupyter

## Now we know about Python
- variables (names) are always references. binding a variable is binding to a reference
- beware mutability, yo. Almost everything except for strings and tuples are mutable, by default.
```python
data = [1, 2, 3]
def append_element(some_list, element):
    some_list.append(element)

append_element(data, 4)
data
```
- `"5" + 5` is a type error (thank goodness)
- isinstance(argument, type), `isinstance(4, int)`, `isinstance(4, (int, float))`, or other tuples work in the 2nd argument

## Tab autocomplete
- `x = "banana"`
- type out `x.` then press Tab to access available methods

```python
def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError: #not iterable
        return False
```

- can compare lists with `==`

## Dealing with strings
- `print(r"ba\na\na")` vs `print("ba\na\na")`
- r next to a string stans for raw
- f next to a string calls format

## Date and time
- `from datetime import datetime, date, time`


## Tuples
- immutable, yay!
-
 `tuple("banana")` and `tuple([1, 2, 3])` makes a tuple of the sequence or iterator
- Unpacking tuples is an awful lot like array destructuring
- `a, b, *rest = (1, 2, 3, 4, 5)`


## Speed considerations
.insert costs more than .append

Basic form of list comprehension is `[expr for val in collection if condition]`
```python
strings = ["a", "as", "abba", "zappa", "affirmation"]
result = [x.upper() for x in strings if len(x) > 2]
other = [x for x in strings if len(x) > 2]
```
Dictionary comprehension
```python
dict_comp = {key-expr: value-expr for value in collection if condition}
```
