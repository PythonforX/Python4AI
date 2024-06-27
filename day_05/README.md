# Strings and File Operations

## Strings in Python

Strings in Python are sequences of characters enclosed in single quotes (`' '`) or double quotes (`" "`). Triple quotes (`''' '''` or `""" """`) are used for multi-line strings.

### Creating Strings

```python
single_quote_string = 'Hello'
double_quote_string = "World"
multi_line_string = '''This is
a multi-line
string.'''
```

### Basic Operations

#### Concatenation

```python
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # "Hello World"
print(result)
```

#### Repetition

```python
str1 = "Hello"
result = str1 * 3  # "HelloHelloHello"
print(result)
```

#### Length

```python
str1 = "Hello"
length = len(str1)  # 5
print(length)
```

### String Indexing and Slicing

#### Indexing

```python
str1 = "Hello"
first_char = str1[0]  # 'H'
last_char = str1[-1]  # 'o'
print(first_char, last_char)
```

#### Slicing

```python
str1 = "Hello, World!"
substring = str1[0:5]  # 'Hello'
print(substring)
```

### Common String Methods

#### `upper()` and `lower()`

```python
str1 = "Hello"
upper_str = str1.upper()  # 'HELLO'
lower_str = str1.lower()  # 'hello'
print(upper_str, lower_str)
```

#### `strip()`

```python
str1 = "   Hello   "
stripped_str = str1.strip()  # 'Hello'
print(stripped_str)
```

#### `split()`

```python
str1 = "Hello, World!"
words = str1.split(", ")  # ['Hello', 'World!']
print(words)
```

#### `join()`

```python
words = ['Hello', 'World']
sentence = " ".join(words)  # 'Hello World'
print(sentence)
```

#### `find()` and `replace()`

```python
str1 = "Hello, World!"
index = str1.find("World")  # 7
new_str = str1.replace("World", "Python")  # 'Hello, Python!'
print(index, new_str)
```

#### `startswith()` and `endswith()`

```python
str1 = "Hello, World!"
print(str1.startswith("Hello"))  # True
print(str1.endswith("World!"))   # True
```

#### `count()`

```python
str1 = "Hello, World!"
count_l = str1.count("l")  # 3
print(count_l)
```

#### `isalpha()`, `isdigit()`, `isalnum()`

```python
str1 = "Hello"
str2 = "12345"
str3 = "Hello123"
print(str1.isalpha())  # True
print(str2.isdigit())  # True
print(str3.isalnum())  # True
```

### String Formatting

#### `%` Operator

```python
name = "John"
age = 30
formatted_str = "My name is %s and I am %d years old." % (name, age)
print(formatted_str)
```

#### `format()` Method

```python
formatted_str = "My name is {} and I am {} years old.".format(name, age)
print(formatted_str)
```

#### f-Strings (Python 3.6+)

```python
formatted_str = f"My name is {name} and I am {age} years old."
print(formatted_str)
```

### Example Usage

Here's a complete example demonstrating various string operations and methods:

```python
# Creating strings
greeting = "Hello, World!"

# Basic operations
full_greeting = greeting + " How are you?"
print(full_greeting)

# Indexing and slicing
first_char = greeting[0]
hello = greeting[:5]
print(first_char, hello)

# String methods
upper_greeting = greeting.upper()
stripped_greeting = greeting.strip()
print(upper_greeting, stripped_greeting)

# Splitting and joining
words = greeting.split(", ")
joined = " - ".join(words)
print(words, joined)

# Finding and replacing
index = greeting.find("World")
new_greeting = greeting.replace("World", "Python")
print(index, new_greeting)

# String formatting
name = "Alice"
age = 25
formatted_str = f"Hello, {name}! You are {age} years old."
print(formatted_str)
```


## File Operations in Python

### Opening a File

You open a file using the `open()` function, which returns a file object. You need to specify the file name and the mode in which you want to open the file.

```python
file = open('filename', 'mode')
```

### File Modes

Common modes include:

- `'r'`: Read (default mode). Opens the file for reading.
- `'w'`: Write. Opens the file for writing (creates a new file or truncates an existing file).
- `'a'`: Append. Opens the file for writing, appending to the end of the file if it exists.
- `'b'`: Binary mode. Opens the file in binary mode (useful for non-text files).
- `'t'`: Text mode (default). Opens the file in text mode.
- `'r+'`: Read and write mode. Opens the file for both reading and writing.

### Closing a File

Always close a file after you’re done using it to free up system resources.

```python
file.close()
```

Using the `with` statement ensures the file is properly closed after its suite finishes, even if an exception is raised.

```python
with open('filename', 'mode') as file:
    # Perform file operations
```

### Reading from a File

#### Reading the Entire Content

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

#### Reading Line by Line

```python
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

#### Reading Specific Number of Characters

```python
with open('example.txt', 'r') as file:
    content = file.read(10)  # Reads the first 10 characters
    print(content)
```

#### Reading All Lines into a List

```python
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
```

### Writing to a File

#### Writing a String to a File

```python
with open('example.txt', 'w') as file:
    file.write("Hello, World!")
```

#### Writing Multiple Lines

```python
with open('example.txt', 'w') as file:
    lines = ["First line\n", "Second line\n", "Third line\n"]
    file.writelines(lines)
```

### Appending to a File

```python
with open('example.txt', 'a') as file:
    file.write("Appending a new line\n")
```

### Example: Reading and Writing

Here’s a full example demonstrating both reading from and writing to a file:

```python
# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")

# Appending to the file
with open('example.txt', 'a') as file:
    file.write("Appending more content.\n")

# Reading from the file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

### File Methods

#### `read()`

Reads the entire file or a specified number of characters.

#### `readline()`

Reads a single line from the file.

```python
with open('example.txt', 'r') as file:
    first_line = file.readline()
    print(first_line)
```

#### `readlines()`

Reads all lines and returns them as a list of strings.

#### `write()`

Writes a string to the file.

#### `writelines()`

Writes a list of strings to the file.

#### `tell()`

Returns the current position of the file pointer.

```python
with open('example.txt', 'r') as file:
    file.read(10)
    position = file.tell()
    print(position)  # Current position in the file
```

#### `seek()`

Moves the file pointer to a specified position.

```python
with open('example.txt', 'r') as file:
    file.seek(5)
    content = file.read()
    print(content)
```

### Binary File Operations

When dealing with binary files, use `'b'` mode.

```python
# Writing to a binary file
with open('example.bin', 'wb') as file:
    file.write(b'\xDE\xAD\xBE\xEF')

# Reading from a binary file
with open('example.bin', 'rb') as file:
    data = file.read()
    print(data)
```

## Summary

- **Opening a File**: Use `open('filename', 'mode')` to get a file object.
- **Modes**: `'r'`, `'w'`, `'a'`, `'b'`, `'t'`, `'r+'`.
- **Reading**: Use `read()`, `readline()`, `readlines()`.
- **Writing**: Use `write()`, `writelines()`.
- **Appending**: Use `'a'` mode with `write()`.
- **File Methods**: `tell()`, `seek()`.
