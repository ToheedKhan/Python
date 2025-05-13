# Functions
Python function features: ***args** and ****kwargs** — along with **lambda** functions.
** Function as First-Class Citizen**
Both Swift and Python treat functions as first-class citizens (you can pass them around like variables).

✅ Basic Function Syntax:
```
def function_name(parameters):
    # code block
    return result
```

## Function Arguments and parameters

**Parameters**: Variables listed in a function's definition.

**Arguments**: Actual values passed to the function when it is called.

**Parameter types**
- default parameters
- arbitary parameters (args)
- keyword parameters (kwargs)

🧩 1. ***args – Variable Positional Parameters**
Allows you to pass any number of positional arguments to a function:
```
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3))  # Output: 6
```
**args** is a **tuple** of all passed arguments.

🧩 2.** **kwargs – Variable Keyword Parameters**
Allows you to pass any number of named keyword arguments and store them in the form of dictionay. Parameter name is mandatoey while calling the function:
```
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_info(name="Alice", age=30)
# Output:
# name = Alice
# age = 30

```

**kwargs** is a **dictionary** of the named arguments.

⚡ 3. **Lambda Function – Short Anonymous Function**

```
square = lambda x: x * x
print(square(5))  # Output: 25
```

Use case: quick functions, often used with **map(), filter()**, etc.

```
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # Output: [1, 4, 9, 16]

```

  ## Default Parameters

  🔹 Function with Default Parameter:
```
def greet(name="Guest"):
    return f"Hello, {name}!"
```

**🧪 Example: Process Numbers with Options**

```
def process_numbers(*args, operation="square", **kwargs):
    if operation == "square":
        func = lambda x: x ** 2
    elif operation == "double":
        func = lambda x: x * 2
    else:
        func = lambda x: x  # identity function (no change)

    results = [func(x) for x in args]

    if kwargs.get("reverse"):
        results.reverse()
    
    return results

# Usage:
print(process_numbers(1, 2, 3, 4, operation="double"))         
# Output: [2, 4, 6, 8]

print(process_numbers(5, 6, 7, reverse=True))                  
# Output: [49, 36, 25] – default operation is square

print(process_numbers(10, 20, 30, operation="none", reverse=True)) 
# Output: [30, 20, 10]

```


 **What’s Happening?**
*args lets you pass any number of numbers.

operation controls the lambda logic (square, double, etc.).

**kwargs allows extra optional settings like reverse.

# In-Built functions
print()
abs()
rount()
filter()
map()
Aggregation functions: sum(), max(), min()

# Python Modules
- Modules refer to a file containing Python code.
- Modules are used to break down large programs into small manageable and organized files.

**To import all available functions -** 
```
import math
```
**To import only one function**
```
from math import gcd
```
**To print Module available functions-**

``
print(dir(math))
``
**Inbuilt Modules**
    - os
    - math
    - random

## Custom Modules

## What is __name__ == '__main__' ?
__name__ == '__main__' means you are directly running the file or program from the main memory.
If you are executing __name__ from different file it will return module name.
