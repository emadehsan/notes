# Notes on Data Structures and Algorithms

## Peculiarities of Python

### Add an item to an iterable while iterating over it?
#### 1. deque
Modifying while iterating over indices (e.g., `range(len(q))`) is generally safe, but directly iterating over the deque can cause infinite loops.
```py
from collections import deque

q = deque([1, 2, 3])

for _ in range(len(q)):  # len(q) evaluated once
	q.append(4)
	print(q)

deque([1, 2, 3, 4])
deque([1, 2, 3, 4, 4])
deque([1, 2, 3, 4, 4, 4])
```

but iterating as an iterator:
```py
from collections import deque

q = deque([1, 2, 3])

for item in q:
	print(item)
	q.append(4)

1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: deque mutated during iteration
```

#### 2. set
Raises a RuntimeError if modified during iteration.
```py
s = {1, 2, 3}

for item in s:  # set only allows this type of iteration
	print(item)
	s.add(4)

1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: Set changed size during iteration
```

#### 3. list
Modifying can lead to infinite loops or skipped elements; use copies to avoid issues.
```py
lst = [1, 2, 3]

for item in lst:
	print(item)
	lst.append(4)

1
2
3
4
4
4
... infinitely many
```

using len(lst) to avoid infinite loop:
```py
lst = [1, 2, 3]

for i in range(len(lst)):
	print(lst[i])
	lst.append(4)
1
2
3
```

removal during iteration:
```py
for item in lst:
	if item % 2 == 0:
		lst.remove(item)
	print(lst)

[1, 2, 3, 4, 5]
[1, 3, 4, 5]
[1, 3, 5]
```

#### 4. dict
Raises a RuntimeError if modified during iteration; iterate over a list of keys to modify safely.

```py
d = {'a': 1, 'b': 2}

for key in d:
	print(key)
	d['c'] = 3

a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: dictionary changed size during iteration
```

### Tuple
tuple, when initialized with a single value, should be defined as 
```py
ab = (1,)

# just doing the following will be evaluated to int
ab = (1)
# type(ab)
# <class 'int'>

# but following is still a tuple
ab = () 

# so is
ab = (1,2)
```

### List Comprehensions

#### 1. List vs Generator (not tuple)
```py
# this returns a list
a_list = [x * x for x in range(5)]
# [0, 1, 4, 9, 16]

# this returns a generator, not a tuple
gen = (x * x for x in range(5))
# <generator object <genexpr> at 0x1007e58a0>

for item in gen:
  print(item)
```

#### 2. Scopes
```py
x = 10
squares = [x * x for x in range(5)] # this x is local to the list comprehension
print(x)  # Outputs: 10
```

#### 3. Late binding in Closures
When using functions inside list comprehensions that capture loop variables, all functions may capture the same (last) value due to late binding.

```py
funcs = [lambda: x for x in range(5)]
results = [f() for f in funcs]
print(results)  # Outputs: [4, 4, 4, 4, 4]

# Solution: Use default arguments to capture the current value of x.
funcs = [lambda x=x: x for x in range(5)]
results = [f() for f in funcs]
print(results)  # Outputs: [0, 1, 2, 3, 4]
```

#### 4. Order of Execution with Multiple Loops
```py
# The order of execution is equivalent to a nested for loop. The first loop is the outer loop, and the last/right loop is the innermost loop:
>>> [x for x in range(5) for y in range(2)]
[0, 0, 1, 1, 2, 2, 3, 3, 4, 4]

# but here first loop is the inner loop, and the last/right loop is the outer loop:
>>> [[x for x in range(5)] for y in range(2)]
[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
```

#### 5. Misplacing the 'if' Clause

```py
# filtering in list comprehension: 
[x for x in range(5) if x % 2 == 0]

# incorrect syntax
[x if x % 2 == 0 for x in range(5)]
SyntaxError: expected 'else' after 'if' expression

# but using as ternary operator is different
[x if x % 2 == 0 else -x for x in range(5)]
```

