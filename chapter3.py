dance_moves = ['mashed potato', 'twist', 'washing machine', 'lawn mower', 'sprinkler', 'tootsie roll', 'electric slide']
numbers = [65, 22, 11, 31, 652, 44, 12, 5, 0, -11]

# .sort() mutates the original list
numbers.sort()
print(numbers)

# sorted returns an altered copy
sorted_by_length = sorted(dance_moves, key=len)

print(sorted_by_length)


fruit = "banana"
print(fruit[2:5])


# we may be tempted to do
# i = 1
# for value in numbers:
#     i += 1
collection = ["mango", "banana", "guava"]
mapping = {}
for i, v in enumerate(collection):
    mapping[v] = i

print(mapping)

# Currying = partial argument application

def add_numbers(a, b):
    return a + b

def add_five(a)
    return add_numbers(5, a)


# Generators
def squares(n=10):
    print("Generating squares from 1 to {0} ".format(n **2))
    for i in range(1, n + 1):
        yield i ** 2

for square in squares():
    print(square)

## generator expressions
# generators feel like lazy sequences
gen = (x ** 2 for x in range(100))

# itertools module is a collection of pre-built generators
# https://docs.python.org/3/library/itertools.html
# “iterator algebra” making it possible to construct specialized tools succinctly and efficiently in pure Python.
# these appear, to me, to be lazy lists or lazy sequence methods


# Exceptions
def attempt_float(x):
    try:
        return float(x)
    except:
        return x

attempt_float("2.3")
attempt_float("banana")


# reading files
# open and close files
path = "examples/segismundo.txt"

# "with" automatically closes the file resource
with open(path) as f:
    lines = [x.rstrip() for x in f]
print(lines)

