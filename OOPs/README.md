# Swift vs Python class

| Feature          | Python                               | Swift                                    |
| ---------------- | ------------------------------------ | ---------------------------------------- |
| Type safety      | Dynamically typed                    | Statically typed                         |
| Access modifiers | Not enforced strictly (`_` for hint) | `public`, `private`, `fileprivate`, etc. |
| Initializer      | `__init__` method                    | `init()` method                          |
| Inheritance      | `class B(A):`                        | `class B: A {}`                          |
| Optional values  | Use `None`                           | Use `?`, `!`                             |
| Deinitializer    | `__del__()`                          | `deinit {}`                              |


# Constructor
Python uses the __init__ method as a constructor inside a class.
Constructor is basically a special member function of a class that is executed automatically whenever we create new objects of a class, so you
don't have to call this function.

```
class Person:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p.name)  # Alice

```



🔍 **Key Differences:**

| Feature           | Python                        | Swift                             |
| ----------------- | ----------------------------- | --------------------------------- |
| Constructor name  | `__init__`                    | `init`                            |
| Type declarations | Not required                  | Required                          |
| Self keyword      | `self` must always be used    | `self` sometimes optional         |
| Optional values   | Use `None` and optional logic | Use `?`, `!` and `Optional` types |

# Definig instanse method

```
def introduce(self):
```
# Constants
In Python, constants are typically defined using **uppercase** variable names by convention, but Python doesn't have true constants (like let in Swift or final in Java). Here's how it's commonly done:
✅ 1. Using Naming Convention (Recommended)
```
PI = 3.14159
MAX_USERS = 100
APP_NAME = "MyApp"
```

✅ 2. Using a Class to Group Constants
```
class Settings:
    API_KEY = "123456"
    TIMEOUT = 30
```

You can access them like `Settings.API_KEY`.

🚫 Python Doesn’t Enforce Immutability
Even though PI is written in all caps, Python won't stop you from reassigning:
```
 PI =3.14
```

🧪 If You Want True Immutability (Optional)
Use a `namedtuple`, `frozen dataclass`, or even third-party libraries like `environs` or `pydantic`.

```
from dataclasses import dataclass

@dataclass(frozen=True)
class Constants:
    PI: float = 3.14159
    MAX_USERS: int = 100

c = Constants()
# c.PI = 3.14  # ❌ Will raise FrozenInstanceError
```

# class variable
In Python, a class variable is a variable that is **shared among all instances of a class**. It's defined inside the class, but outside of any instance methods (like __init__).
They are not associated with the class.
Ex- class variables can be used in counting instances

```
class Dog:
    species = "Canis familiaris"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris
```

**Swift vs Python**

| Feature              | Python                    | Swift                               |
| -------------------- | ------------------------- | ----------------------------------- |
| Syntax               | `ClassName.var_name`      | `static var varName`                |
| Access via instance  | Yes (but not recommended) | No (must use class name)            |
| Mutable              | Yes                       | Yes                                 |
| Override in subclass | Yes                       | Use `class var` (for computed only) |


# Magic Functions in class

In Python, magic functions (also called dunder methods, because they begin and end with double underscores like __init__, __str__, etc.) are special methods that give classes special behavior, especially with operators and built-in functions.
**Called automatically when an event occur.**
`dir(obj)` list out all available functions

| Method                     | Purpose                                                                 |
| -------------------------- | ----------------------------------------------------------------------- |
| `__init__`                 | Constructor; called when an object is created                           |
| `__str__`                  | Defines the “informal” string representation (`str(obj)`, `print(obj)`) |
| `__repr__`                 | Defines the “official” representation (`repr(obj)`)                     |
| `__len__`                  | Defines behavior for `len(obj)`                                         |
| `__getitem__`              | Enables indexing like `obj[key]`                                        |
| `__setitem__`              | Enables item assignment like `obj[key] = value`                         |
| `__eq__`                   | Equality check (`==`)                                                   |
| `__lt__`, `__gt__`, etc.   | Comparisons (`<`, `>`, etc.)                                            |
| `__add__`, `__sub__`, etc. | Arithmetic operators (`+`, `-`, etc.)                                   |
| `__call__`                 | Makes an object callable like a function                                |
| `__del__`                  | Called when an object is deleted (destructor)                           |
| `__contains__`             | Used for `in` keyword, like `x in obj`                                  |



# OOPs

# Encapsulation
Wrapping up of data under one unit, under one name.

# Inheritance

## 🆚 Python vs Swift: Inheritance Comparison

| Feature                   | 🐍 Python                                      | 🕊 Swift                                                   |
|---------------------------|-----------------------------------------------|------------------------------------------------------------|
| **Class Declaration**     | `class SubClass(SuperClass):`                 | `class SubClass: SuperClass {}`                            |
| **Method Override**       | Redefine the method without keyword            | Must use `override` keyword                                |
| **Multiple Inheritance**  | ✅ Yes                                          | ❌ No (Use protocols instead)                               |
| **Constructors**          | `__init__()`                                   | `init()`                                                    |
| **Access Control**        | Convention-based (`_var`, `__var`)             | Explicit: `public`, `private`, `internal`, `fileprivate`    |
| **Super Keyword**         | `super().method()`                             | `super.method()`                                           |
| **Protocol Usage**        | Optional (via ABCs or duck typing)             | Strongly encouraged (`protocol`, protocol-oriented design) |

---

### 🧪 Example Code

#### Python
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()
```

✅ Summary

| Concept              | Python        | Swift                  |
| -------------------- | ------------- | ---------------------- |
| Inheritance Style    | Class-based   | Class + Protocol-based |
| Multiple Inheritance | ✅ Yes         | ❌ No (use protocols)   |
| Syntax Simplicity    | More flexible | More strict and safe   |

🧨 **Problems with Multiple Inheritance**
**Diamond Problem (Ambiguity in Method Resolution)**

When two parent classes inherit from the same grandparent class, and the child inherits from both parents.

**Python uses Method Resolution Order (MRO)** to resolve this, but it can still cause confusion.

```
class A:
    def greet(self): print("Hello from A")

class B(A):
    def greet(self): print("Hello from B")

class C(A):
    def greet(self): print("Hello from C")

class D(B, C): pass

d = D()
d.greet()  # Output? Depends on MRO: B → C → A

```

**Increased Complexity**

Makes code harder to read and debug.

Developers need to understand the inheritance hierarchy deeply.

**Tight Coupling**

Subclasses become tightly coupled with all parent classes.

Changes in one base class might unintentionally break subclasses.

**Unexpected Method Overrides**

If parent classes have methods with the same name but different logic, it might be unclear which one gets called.

**Constructor Conflict**

If multiple base classes have __init__ methods, the child needs to call them manually or via super(), and order matters.

🧭** Best Practices**
Prefer** composition over inheritance** when possible.

Use interfaces or protocols (like in Swift) for shared behavior.

In Python, use **super()** carefully and understand the MRO (ClassName.__mro__) if you're using multiple inheritance.

# 🧩 Python Alternatives to Swift Protocols
✅ 1. **Abstract Base Class (ABC)**
✅ 2. **Typing Protocol (Python 3.8+)**

## Summary

| Feature                 | Swift Protocol        | Python Equivalent             |
| ----------------------- | --------------------- | ----------------------------- |
| Interface by contract   | `protocol`            | `abc.ABC`, `@abstractmethod`  |
| Structural subtyping    | Protocol with `where` | `typing.Protocol`             |
| Default implementations | Protocol extensions   | Mixin classes or base classes |


# What is Polymorphism?
Polymorphism means “**many forms**” — it allows objects of different classes to be treated through a common interface.

🔷 **Swift Polymorphism**
✔️ **Achieved through:**
    - Protocols
    - Inheritance

🟡 **Python Polymorphism**
✔️ **Achieved through:**
   - Duck Typing
   - Inheritance
   - Abstract Base Classes (ABC) (optional)

⚖️ **Comparison Table**

| Feature                 | Swift                                   | Python                                 |
| ----------------------- | --------------------------------------- | -------------------------------------- |
| **Typing**              | Static                                  | Dynamic                                |
| **How it's enforced**   | Protocols or base classes               | Duck typing or ABC module              |
| **Requires base type?** | Yes (Protocol or Superclass)            | No (can just call method if exists)    |
| **Use in collections**  | Yes (must conform to protocol or class) | Yes (any object with matching methods) |
| **Runtime Safety**      | Compile-time checking                   | Runtime errors if method not found     |

