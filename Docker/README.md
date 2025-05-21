# Python

**Python for Data Science Master Course** 💻

https://github.com/coding-minutes/python-data-science-mastercourse

## To find sqaure
**Use ** **
 ex- x**2

**Square Root**

 x = x**0.5


 # Loop

 ## Example 1: Loop through a list
 for item in sequence:
  fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

 ## Example 2: Using range() to loop over numbers
 for i in range(5):
    print(i)
## Example 3: Loop with start, stop, step
for i in range(2, 10, 2):  # from 2 to 9, step by 2
    print(i)
## Nested for loop
for i in range(3):         # Outer loop
    for j in range(2):     # Inner loop
        print(f"i={i}, j={j}")

## for-else in Python
The **else** block runs only if the loop completes without a break.

Example: Check if a number is prime

    ```
n = 7
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        print("Not prime")
        break
else:
    print("Prime")
    ```

## while-else :
The else block runs only if the loop ends naturally (not by break).

# String

## Multiline string
In Python, """ """ (triple double quotes) or ''' ''' (triple single quotes) are used for **multiline strings or docstrings**.
```
message = """This is a
multiline string in Python.
It spans several lines."""
print(message)
```

 **Docstring (Documentation String)**
Docstrings describe what a module, class, or function does.
```
def greet():
    """This function prints a greeting message."""
    print("Hello!")

print(greet.__doc__)  # Accessing the docstring

```
✅ **Notes**:
You can use ''' or """ — both are functionally the same.

Docstrings are usually written using """ """ by convention.

They're accessible using the .__doc__ attribute.

**Formating**
Using `str.format()` — an older string formatting method in Python.
```
print("{} is already dead".format(self.name)) 
```
**Python 3.6**
The `f in print(f"...")` stands for f-string, short for **formatted string literal**

```
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

```
📌 Benefits of f-strings:
Cleaner and more readable than using + or format()

Can include expressions too:
```
print(f"Next year I will be {age + 1} years old.")
```

✅ What It Does:
It allows you to embed variables directly inside a string using {}.

**Negative indexing**
In other language we access last character by writing len(str) -1. But Python supports negative indexing as well.
str[-1] will automatically return last character
str[-2] will return 2nd last character.

## String slicing
str[start_idx: end_idx+1]

**To access all characters except last two characters**
str[:-2]

** For concatenation use **+** **

## Multiplication

# Multiplication of string with int n results into repitation string n times.
ex- "hello"*4

## Palindrom exapmle
```
def is_clean_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
```

**my way **
```
x  = int(len(s) / 2)

isPalindrome = True

for i in range(x):
   if s[i] != s[-(i+1)]:
       isPalindrome = False
       break
   
print(isPalindrome)
```
## Count number of vowels
  
  ```
    def count_vowels(s):
       return sum(1 for char in s if char in "aeiouAEIOU")
  ```
1 for char in s if char in "aeiouAEIOU":

This is a generator expression (a compact form of a loop) that produces a 1 for each character that is a vowel.

For example, if s = "Hello", the generator will yield 1 for the vowel 'e' and 'o'.

**sum(...):**

sum() calculates the total of all the 1s produced by the generator expression.

# List
Can storeheterogenous elements.
## List Functions
my_list.sort() -> ascemding order
my_list.sort(reverse=True) -> Descending order

# Find element in list
Use **in** and **not in** operator (Work with string and list both)
ex- 99 in my_list

# List Comprehension

**Basic Syntax**
[expression for item in iterable]

**With Condition:**
[expression for item in iterable if condition]

```
squares = [x * x for x in range(10) if x % 2 == 0]
```

# List Operation

```lst1 = [2, 3, 4, 5]
lst2 = [1, 2, 3, 4, 5]
```

✅ 1. Find elements in lst2 but not in lst1:
diff = [x for x in lst2 if x not in lst1]
print(diff)  # Output: [1]

✅ 2. Find common elements:
common = [x for x in lst1 if x in lst2]
print(common)  # Output: [2, 3, 4, 5]

 ✅ 3. Union (without duplicates):
 union = list(set(lst1 + lst2))
print(union)  # Output: [1, 2, 3, 4, 5]

✅ 4. Check if lst1 is a subset of lst2:
is_subset = all(x in lst2 for x in lst1)
print(is_subset)  # Output: True

## List Concatenation (+)

 **Explanation:**
The + operator concatenates the two lists.

- It does not remove duplicates.

- It creates a new list containing the elements of both. The order is preserved: first lst1, then lst2.
- It does not modify the original lists.


```
result = list1 + list2
print(result)  # Output: [2, 3, 4, 5, 1, 2, 3, 4, 5]
```

# Duck typing
In Python, duxk typing is a programming concept where an object’s behavior is more important than its actual type.
🦆 **Definition**
"If it walks like a duck and quacks like a duck, it’s a duck."

In Python, you don’t check if an object is of a specific class — you just check if it has the methods/attributes you need.

# Why It Matters
Encourages flexible and loosely-coupled code.

Python emphasizes behavior over type, which is great for polymorphism.




