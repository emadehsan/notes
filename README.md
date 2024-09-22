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
