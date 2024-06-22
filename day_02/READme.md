### 1. Conditional Statements
Conditional statements allow you to execute code blocks based on certain conditions.

#### if Statement
Executes a block of code if the condition is `True`.

```python
if condition:
    print("Condition is true")
```

#### elif Statement
Checks another condition if the previous conditions are `False`.

```python
if condition1:
    print("Condition1 is true")
elif condition2:
    print("Condition2 is true")
```

#### else Statement
Executes a block of code if none of the previous conditions are `True`.

```python
if condition1:
    print("Condition1 is true")
elif condition2:
    print("Condition2 is true")
else:
    print("None of the conditions are true")
```

### 2. Looping Statements
Looping statements allow you to execute a block of code multiple times.

#### for Loop
Iterates over a sequence (such as a list, tuple, or string).

```python
for item in sequence:
    print(item)
```

Example:

```python
for i in range(5):
    print(i)
```

#### while Loop
Executes a block of code as long as the condition is `True`.

```python
while condition:
    print("Condition is true")
```

Example:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### 3. Control Flow Statements
Control flow statements change the normal flow of execution of loops.

#### break Statement
Exits the loop prematurely when a certain condition is met.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

#### continue Statement
Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

#### pass Statement
Does nothing and is used as a placeholder.

```python
if condition:
    pass  # TODO: implement later
```

### Summary
Control structures are essential for directing the flow of execution in a program:

- **Conditional Statements** (`if`, `elif`, `else`): Use to make decisions in your code.
- **For Loops** (`for`): Use to iterate over a sequence.
- **While Loops** (`while`): Use to repeat a block of code as long as a condition is true.
- **Break Statement** (`break`): Use to exit a loop prematurely.
- **Continue Statement** (`continue`): Use to skip to the next iteration of a loop.
- **Pass Statement** (`pass`): Use as a placeholder for future code.

These structures allow you to write complex and efficient programs by controlling the flow of execution based on various conditions and repetitive tasks.