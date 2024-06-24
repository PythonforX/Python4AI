# Python Functions 

Functions in Python are reusable pieces of code that perform a specific task. They help to make programs more modular, manageable, and readable. This tutorial will guide you through the basics of functions in Python, complete with simple and unique examples.

#### Table of Contents
1. [Defining a Function](#defining-a-function)
2. [Calling a Function](#calling-a-function)
3. [Function Parameters](#function-parameters)
4. [Return Statement](#return-statement)
5. [Default Parameters](#default-parameters)
6. [Keyword Arguments](#keyword-arguments)
7. [Variable-length Arguments](#variable-length-arguments)
8. [Lambda Functions](#lambda-functions)
9. [Function Annotations](#function-annotations)

---

### 1. Defining a Function

A function is defined using the `def` keyword, followed by the function name, parentheses, and a colon. The function body contains the code that executes when the function is called.

```python
def greet():
    print("Hello, World!")
```

### 2. Calling a Function

To execute the function, you simply call it by its name followed by parentheses.

```python
greet()  # Output: Hello, World!
```

### 3. Function Parameters

Functions can accept parameters (also known as arguments) that allow you to pass data into them.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

### 4. Return Statement

The `return` statement is used to exit a function and return a value.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

### 5. Default Parameters

You can provide default values for parameters. These default values are used if no argument is passed.

```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet()         # Output: Hello, World!
greet("Alice")  # Output: Hello, Alice!
```

### 6. Keyword Arguments

Keyword arguments are specified by parameter name when calling the function. This makes the function call more readable.

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(animal_type="hamster", pet_name="Harry")
describe_pet(pet_name="Willie", animal_type="dog")
```

### 7. Variable-length Arguments

Sometimes, you might want to pass a variable number of arguments to a function. This can be done using `*args` for non-keyword arguments and `**kwargs` for keyword arguments.

```python
def make_pizza(size, *toppings):
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(12, "pepperoni", "mushrooms", "green peppers")
```

```python
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
```

### 8. Lambda Functions

Lambda functions are small anonymous functions defined using the `lambda` keyword. They are useful for short, throwaway functions.

```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

# Another example:
squared = lambda x: x ** 2
print(squared(4))  # Output: 16
```

### 9. Function Annotations

Function annotations provide a way of attaching metadata to function arguments and return values. They have no impact on the function's behavior but can be used for type checking, documentation, and more.

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```

### Summary

- **Defining Functions**: Use the `def` keyword.
- **Calling Functions**: Use the function name followed by parentheses.
- **Function Parameters**: Pass data into functions using parameters.
- **Return Statement**: Return values from functions using `return`.
- **Default Parameters**: Specify default values for parameters.
- **Keyword Arguments**: Use parameter names to specify arguments.
- **Variable-length Arguments**: Use `*args` and `**kwargs` for variable arguments.
- **Lambda Functions**: Use the `lambda` keyword for small anonymous functions.
- **Function Annotations**: Attach metadata to function parameters and return values.

With these concepts, you can create more organized, reusable, and readable Python code.