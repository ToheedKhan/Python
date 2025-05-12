# Tuples

 - Similar to list (read only)
 - Ordered collection of items
 - Indexable
 - Immutable

   **Tuples are faster than list**
   Use to store sensitive data that cannot be changed. Eg - Employe Salary, value of pi constant etc

## Tuple creation

**Use () to declare **
```
tup = (8, 9, "Hello", 88)
print(tup) // (8, 9, Hello, 88)
type(tup) // tuple
print( tup[0] ) // 8
print( tup[:-1] ) //print all except last
```

# Set
  - Contains only unique elements
  - Mutable
  - Unordered
  - Unindexable

    **Use {} to declare the set**
    Available methods **add()** and **remove()**

    **Constructor**
    set()
    my_list = [1, 2,1,3]
    my_set = Set(my_list)

# Dictionay
 - Store data in key-value pair (Tabular data)
 - Unordered
 - unindexable
 - access the value with the help of key

   **Use {:} to declare**

   ```
   Access using dic['name'] # returns error if key not found

   use **dic.get()** tp avoid errors
   
    value = dict.get("apple")         # returns value or None if key not found
   ```

   **Default Value Handling**
   ```
   value = dict.get("orange", 0)     # default to 0
   ````
    **To display key values combined in a pair.**
   ```
   dic.items()  # returns (key, value) pair in tuple
   
   for k,v in dic.items():
       print(k, " : ", v)
   ```

   **To delete key, value**
   ```
   dic.pop('name') # return deleted values as well if you want to store you can
   ``` 

   
