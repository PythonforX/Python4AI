### Functions in Python

**1. Definition:**
   - A function is a block of organized, reusable code that performs a single action.

**2. Syntax:**
   - Functions are defined using the `def` keyword.

**3. Function Definition:**
   ```python
   def function_name(parameters):
       """Docstring explaining the function."""
       # Function body
       return value
   ```

**4. Example without Parameters:**
   ```python
   def greet():
       print("Hello, world!")
   greet()  # Output: Hello, world!
   ```

**5. Example with Parameters:**
   ```python
   def greet(name):
       print(f"Hello, {name}!")
   greet("Alice")  # Output: Hello, Alice!
   ```

**6. Return Statement:**
   - Functions can return values using the `return` keyword.
   ```python
   def add(a, b):
       return a + b
   result = add(3, 5)
   print(result)  # Output: 8
   ```

**7. Multiple Returns:**
   ```python
   def swap(x, y):
       return y, x
   a, b = swap(1, 2)
   print(a, b)  # Output: 2 1
   ```

**8. Default Parameters:**
   ```python
   def greet(name="World"):
       print(f"Hello, {name}!")
   greet()  # Output: Hello, World!
   greet("Alice")  # Output: Hello, Alice!
   ```

**9. Lambda Functions:**
   - Anonymous single-expression functions.
   ```python
   add = lambda x, y: x + y
   print(add(2, 3))  # Output: 5
   ```

### Summary

- **Defining Functions:** Use `def` keyword.
- **Calling Functions:** Use `function_name()`.
- **Parameters:** Functions can have parameters.
- **Return Values:** Use `return` to send back a result.
- **Lambda Functions:** Short, anonymous functions for simple operations.

Functions help organize code, make it reusable, and improve readability.