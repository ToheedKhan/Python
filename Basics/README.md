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

Negative indexing
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
Use in operator (Work with string and kist both)
ex- 99 in my_list

# List Comprehension





