# Lists

In Python, a list is a versatile and widely used data structure that allows you to store an ordered collection of items. These items can be of any data type, and a single list can hold a mix of data types. Lists are mutable, meaning their elements can be changed after the list has been created.

### Creating Lists

You can create a list by placing all the items (elements) inside square brackets `[]`, separated by commas.

```python
# Creating a list
my_list = [1, 2, 3, 4, 5]

# List with different data types
mixed_list = [1, "hello", 3.14, True]
```

### Accessing List Elements

You can access elements in a list by their index. Python uses zero-based indexing, so the first element has index 0.

```python
# Accessing elements
first_element = my_list[0]  # Output: 1
second_element = my_list[1]  # Output: 2
```

### Modifying Lists

Lists are mutable, meaning you can change their elements after the list has been created.

```python
# Modifying elements
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]
```

### List Methods

Python lists come with several built-in methods for performing common tasks.

1. **`append(x)`**: Adds an item `x` to the end of the list.
    ```python
    my_list.append(6)
    ```

2. **`extend(iterable)`**: Extends the list by appending elements from the iterable.
    ```python
    my_list.extend([7, 8])
    ```

3. **`insert(i, x)`**: Inserts an item `x` at a specified index `i`.
    ```python
    my_list.insert(1, 'a')
    ```

4. **`remove(x)`**: Removes the first item from the list whose value is `x`.
    ```python
    my_list.remove('a')
    ```

5. **`pop([i])`**: Removes and returns the item at the specified index `i`. If no index is specified, `pop()` removes and returns the last item.
    ```python
    my_list.pop(0)
    ```

6. **`clear()`**: Removes all items from the list.
    ```python
    my_list.clear()
    ```

7. **`index(x[, start[, end]])`**: Returns the index of the first item whose value is `x`. The optional arguments `start` and `end` are used to limit the search to a particular subsequence of the list.
    ```python
    index = my_list.index(2)
    ```

8. **`count(x)`**: Returns the number of times the item `x` appears in the list.
    ```python
    count = my_list.count(2)
    ```

9. **`sort(key=None, reverse=False)`**: Sorts the items of the list in place (the arguments can be used for sort customization).
    ```python
    my_list.sort()
    ```

10. **`reverse()`**: Reverses the elements of the list in place.
    ```python
    my_list.reverse()
    ```

11. **`copy()`**: Returns a shallow copy of the list.
    ```python
    new_list = my_list.copy()
    ```

### List Comprehensions

List comprehensions provide a concise way to create lists.

```python
# Creating a list of squares
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

### Slicing Lists

You can access a range of elements using slicing.

```python
# Slicing a list
sub_list = my_list[1:4]  # Output: [5, 4, 3]
```

### Checking for Membership

Use the `in` keyword to check if an item is in the list.

```python
print(3 in my_list)  # Output: True
print(10 in my_list)  # Output: False
```

### List Length

Get the number of items in a list using `len()`.

```python
print(len(my_list))  # Output: 5
```

### Example

Here’s a practical example of using lists in a Python program:

```python
# Creating a list of fruits
fruits = ["apple", "banana", "cherry"]

# Adding a new fruit
fruits.append("orange")

# Removing a fruit
fruits.remove("banana")

# Sorting the list
fruits.sort()

# Printing the final list
print(fruits)  # Output: ['apple', 'cherry', 'orange']
```

# Tuples 

In Python, a tuple is a collection of items that is ordered and immutable, meaning that once a tuple is created, its elements cannot be changed. Tuples are similar to lists in that they can store a heterogeneous collection of items, but unlike lists, they are immutable.

### Creating Tuples

You can create a tuple by placing all the items (elements) inside parentheses `()`, separated by commas.

```python
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Tuple with different data types
mixed_tuple = (1, "hello", 3.14, True)

# Creating a tuple without parentheses (using commas)
another_tuple = 1, 2, 3

# Single-element tuple (note the comma)
single_element_tuple = (1,)
```

### Accessing Tuple Elements

You can access elements in a tuple by their index. Python uses zero-based indexing, so the first element has index 0.

```python
# Accessing elements
first_element = my_tuple[0]  # Output: 1
second_element = my_tuple[1]  # Output: 2
```

### Tuple Methods

Although tuples are immutable, they come with a few built-in methods.

1. **`count(x)`**: Returns the number of times the item `x` appears in the tuple.
    ```python
    count = my_tuple.count(2)
    ```

2. **`index(x[, start[, end]])`**: Returns the index of the first item whose value is `x`. The optional arguments `start` and `end` are used to limit the search to a particular subsequence of the tuple.
    ```python
    index = my_tuple.index(3)
    ```

### Tuple Operations

Even though tuples themselves cannot be modified (immutable), you can perform several operations with them.

- **Concatenation**: Combine two or more tuples using the `+` operator.
    ```python
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    combined_tuple = tuple1 + tuple2  # Output: (1, 2, 3, 4, 5, 6)
    ```

- **Repetition**: Repeat the elements in a tuple using the `*` operator.
    ```python
    repeated_tuple = tuple1 * 2  # Output: (1, 2, 3, 1, 2, 3)
    ```

### Tuple Slicing

You can access a range of elements using slicing.

```python
# Slicing a tuple
sub_tuple = my_tuple[1:4]  # Output: (2, 3, 4)
```

### Unpacking Tuples

You can unpack tuple elements into variables.

```python
# Unpacking
a, b, c = (1, 2, 3)
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
```

### Checking for Membership

Use the `in` keyword to check if an item is in the tuple.

```python
print(3 in my_tuple)  # Output: True
print(10 in my_tuple)  # Output: False
```

### Tuple Length

Get the number of items in a tuple using `len()`.

```python
print(len(my_tuple))  # Output: 5
```

### Example

Here’s a practical example of using tuples in a Python program:

```python
# Creating a tuple of fruits
fruits = ("apple", "banana", "cherry")

# Checking membership
print("banana" in fruits)  # Output: True

# Unpacking the tuple
fruit1, fruit2, fruit3 = fruits
print(fruit1)  # Output: apple
print(fruit2)  # Output: banana
print(fruit3)  # Output: cherry

# Concatenating tuples
new_fruits = fruits + ("orange",)
print(new_fruits)  # Output: ('apple', 'banana', 'cherry', 'orange')

# Counting occurrences
count = new_fruits.count("apple")
print(count)  # Output: 1

# Finding index
index = new_fruits.index("cherry")
print(index)  # Output: 2
```



# Dictionaries

A dictionary is a collection of key-value pairs. Each key is unique and acts as an identifier for its associated value. Dictionaries are mutable, meaning you can change their contents after they are created. They are optimized for retrieving values when the key is known.

### Creating Dictionaries

You can create a dictionary by placing a comma-separated list of key-value pairs within curly braces `{}`, with a colon `:` separating each key from its value.

```python
# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Creating an empty dictionary
empty_dict = {}
```

### Accessing Dictionary Elements

You can access elements in a dictionary by their key.

```python
# Accessing elements
name = my_dict["name"]  # Output: Alice
age = my_dict["age"]  # Output: 25
```

### Modifying Dictionaries

Dictionaries are mutable, so you can change, add, or remove key-value pairs.

```python
# Changing a value
my_dict["age"] = 26

# Adding a new key-value pair
my_dict["email"] = "alice@example.com"

# Removing a key-value pair
del my_dict["city"]

# Using the pop method to remove a key-value pair
email = my_dict.pop("email")
```

### Dictionary Methods

Python dictionaries come with several built-in methods for performing common tasks.

1. **`clear()`**: Removes all items from the dictionary.
    ```python
    my_dict.clear()
    ```

2. **`copy()`**: Returns a shallow copy of the dictionary.
    ```python
    new_dict = my_dict.copy()
    ```

3. **`fromkeys(iterable, value=None)`**: Creates a new dictionary with keys from the given iterable and values set to the given value.
    ```python
    keys = ["name", "age"]
    new_dict = dict.fromkeys(keys, None)
    ```

4. **`get(key, default=None)`**: Returns the value for the specified key if key is in the dictionary, else default.
    ```python
    age = my_dict.get("age", 0)
    ```

5. **`items()`**: Returns a view object that displays a list of dictionary's key-value tuple pairs.
    ```python
    items = my_dict.items()
    ```

6. **`keys()`**: Returns a view object that displays a list of all the keys in the dictionary.
    ```python
    keys = my_dict.keys()
    ```

7. **`pop(key, default=None)`**: Removes the specified key and returns the corresponding value. If the key is not found, returns default.
    ```python
    age = my_dict.pop("age", 0)
    ```

8. **`popitem()`**: Removes and returns the last key-value pair inserted into the dictionary.
    ```python
    last_item = my_dict.popitem()
    ```

9. **`setdefault(key, default=None)`**: Returns the value of the specified key. If the key does not exist, inserts the key with the specified default value.
    ```python
    age = my_dict.setdefault("age", 30)
    ```

10. **`update([other])`**: Updates the dictionary with the key-value pairs from another dictionary or from an iterable of key-value pairs.
    ```python
    my_dict.update({"city": "Boston"})
    ```

11. **`values()`**: Returns a view object that displays a list of all the values in the dictionary.
    ```python
    values = my_dict.values()
    ```

### Example

Here’s a practical example of using dictionaries in a Python program:

```python
# Creating a dictionary of a person's details
person = {"name": "Alice", "age": 25, "city": "New York"}

# Accessing values
print(person["name"])  # Output: Alice

# Adding a new key-value pair
person["email"] = "alice@example.com"

# Updating an existing value
person["age"] = 26

# Removing a key-value pair
del person["city"]

# Using get method to access a value
email = person.get("email")
print(email)  # Output: alice@example.com

# Using items, keys, and values methods
print(person.items())  # Output: dict_items([('name', 'Alice'), ('age', 26), ('email', 'alice@example.com')])
print(person.keys())  # Output: dict_keys(['name', 'age', 'email'])
print(person.values())  # Output: dict_values(['Alice', 26, 'alice@example.com'])

# Copying the dictionary
person_copy = person.copy()

# Clearing the dictionary
person.clear()
print(person)  # Output: {}
```

### Summary

Dictionaries in Python are a powerful and flexible way to store and manipulate key-value pairs. They allow for efficient retrieval, modification, and management of data, making them ideal for use cases where data is identified by unique keys.