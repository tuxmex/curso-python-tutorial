# Flashcard Deck: Python Prep Questions (Kindle 7" Optimized)

Aquí tienes un mazo de flashcards optimizado para Kindle 7" con las 40 preguntas de preparación Python, usando texto grande y diseño simple.

---

**Flashcard 1/40**

**Pregunta:**
What is the expected output of:
```python
from random import randint
for i in range(2):
    print(randint(3,4), end='')
```

**Respuesta:**
34, 43, 33, or 44

---

**Flashcard 2/40**

**Pregunta:**
What is the expected output of:
```python
s = "this is a string"
print(s[2:8])
```

**Respuesta:**
"is is"

---

**Flashcard 3/40**

**Pregunta:**
If you want to import mathematical constant e from math, which line will you use?

**Respuesta:**
`from math import e`

---

**Flashcard 4/40**

**Pregunta:**
What is the output of:
```python
def outer_func(num):
    def inner_func():
        print(num)
    return inner_func

funcs = []
for i in range(3):
    funcs.append(outer_func(i))

for f in funcs:
    f()
```

**Respuesta:**
0
1
2

---

**Flashcard 5/40**

**Pregunta:**
What is the output of:
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
divisor = 3
pairs = [(numbers[i], numbers[j]) for i in range(len(numbers)) 
         for j in range(i+1, len(numbers)) 
         if (numbers[i] + numbers[j]) % divisor == 0]
print(pairs)
```

**Respuesta:**
[(1, 2), (1, 5), (1, 8), (2, 4), (2, 7), (2, 10), (3, 6), (3, 9), (4, 5), (4, 8), (5, 7), (5, 10), (6, 9), (7, 8), (8, 10)]

---

**Flashcard 6/40**

**Pregunta:**
What is the output of:
```python
class MyClass:
    pass

obj = MyClass()
print(hasattr(obj, '__name__'))
print(hasattr(obj, '__module__'))
print(hasattr(obj, '__bases__'))
print(hasattr(MyClass, '__name__'))
```

**Respuesta:**
False
True
False
True

---

**Flashcard 7/40**

**Pregunta:**
Consider the Animal/Dog/Cat classes. What is the type of `fido`?

**Respuesta:**
Dog

---

**Flashcard 8/40**

**Pregunta:**
What is the output of the file handling code?

**Respuesta:**
b'Hello world!'

---

**Flashcard 9/40**

**Pregunta:**
What is the expected output of:
```python
def f(a):
    try:
        a = a / a
    except:
        print('pro', end='')
    else:
        print('code', end='')
    finally:
        print('2U', end='')

f(42)
f(0)
```

**Respuesta:**
code2Upro2U

---

**Flashcard 10/40**

**Pregunta:**
Select valid string operators (two answers)

**Respuesta:**
*= and *

---

**Flashcard 11/40**

**Pregunta:**
What is the output of the private variable code?

**Respuesta:**
20

---

**Flashcard 12/40**

**Pregunta:**
What is the output of the matrix transpose code?

**Respuesta:**
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

---

**Flashcard 13/40**

**Pregunta:**
What is the expected output of:
```python
s = "a,b,c,d,e"
print(s.split(",")[::-1])
```

**Respuesta:**
['e', 'd', 'c', 'b', 'a']

---

**Flashcard 14/40**

**Pregunta:**
What is the output of the multiple inheritance code?

**Respuesta:**
B

---

**Flashcard 15/40**

**Pregunta:**
What is the expected output of:
```python
s = "ProCoding"
print(sorted(s, reverse=True))
```

**Respuesta:**
['r', 'o', 'o', 'n', 'i', 'g', 'd', 'P', 'C']

---

**Flashcard 16/40**

**Pregunta:**
When Python first imports a module where does Python deploy the pyc files?

**Respuesta:**
__pycache__ directory

---

**Flashcard 17/40**

**Pregunta:**
What is the output of:
```python
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
result = [[num1 * num2 for num1 in nums1] for num2 in nums2]
print(result)
```

**Respuesta:**
[[4, 8, 12], [5, 10, 15], [6, 12, 18]]

---

**Flashcard 18/40**

**Pregunta:**
What is the output of:
```python
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def multiply(self, z):
        self.x *= z
        self.y *= z

a = MyClass(2, 3)
a.multiply(2)
print(a.x, a.y)
```

**Respuesta:**
4 6

---

**Flashcard 19/40**

**Pregunta:**
Select code snippets that print True (two answers)

**Respuesta:**
`print(""<"Z")` and `print("20"<"8")`

---

**Flashcard 20/40**

**Pregunta:**
What does "pip list" command do?

**Respuesta:**
It lists all the packages that are installed in the current environment

---

**Flashcard 21/40**

**Pregunta:**
What is the expected output of:
```python
data = [42, 13, -4]
try:
    print(data[-4])
except Exception as exception:
    print(exception.args)
else:
    print("('yes',)")
```

**Respuesta:**
('list index out of range',)

---

**Flashcard 22/40**

**Pregunta:**
What is the output of the Employee class code?

**Respuesta:**
The program will terminate with an error

---

**Flashcard 23/40**

**Pregunta:**
What is the expected behavior of the exception handling code?

**Respuesta:**
The code is erroneous

---

**Flashcard 24/40**

**Pregunta:**
Which statement about try statements is true?

**Respuesta:**
A try statement can have a finally clause without an except clause

---

**Flashcard 25/40**

**Pregunta:**
What is the output of the property code?

**Respuesta:**
Bob

---

**Flashcard 26/40**

**Pregunta:**
What is the output of the class variable code?

**Respuesta:**
1

---

**Flashcard 27/40**

**Pregunta:**
What is the output of the custom exception code?

**Respuesta:**
MyException: This is a custom exception

---

**Flashcard 28/40**

**Pregunta:**
Select true statements about pip (two answers)

**Respuesta:**
You can update packages using `install --upgrade` and `install -U`

---

**Flashcard 29/40**

**Pregunta:**
What happens if user enters "procoding" for x and empty string for y?

**Respuesta:**
The program will print "Zero!"

---

**Flashcard 30/40**

**Pregunta:**
What is the output of the multiple inheritance code?

**Respuesta:**
10 21

---

**Flashcard 31/40**

**Pregunta:**
What is the output of the bytearray file writing code?

**Respuesta:**
A TypeError will be raised because a bytearray is not a string

---

**Flashcard 32/40**

**Pregunta:**
What is the output of the Book/Ebook classes code?

**Respuesta:**
The Catcher in the Rye by J.D. Salinger
To Kill a Mockingbird by Harper Lee [PDF]

---

**Flashcard 33/40**

**Pregunta:**
What is the output of the BankAccount code?

**Respuesta:**
The balance is 100

---

**Flashcard 34/40**

**Pregunta:**
What is the expected output of the string comparisons?

**Respuesta:**
True
True
True

---

**Flashcard 35/40**

**Pregunta:**
Select true statements about string methods (two answers)

**Respuesta:**
find() returns -1 if substring not found, index() raises ValueError
A codepoint is a number that corresponds to a character

---

**Flashcard 36/40**

**Pregunta:**
Which is true about declaring and invoking constructors in Python?

**Respuesta:**
The __init__ method is used to declare the constructor, and it is invoked automatically when an object is created

---

**Flashcard 37/40**

**Pregunta:**
What is the output of the file writing exception code?

**Respuesta:**
"Permission denied"

---

**Flashcard 38/40**

**Pregunta:**
What is the output of the object reference code?

**Respuesta:**
30

---

**Flashcard 39/40**

**Pregunta:**
What is the output of the nested function code?

**Respuesta:**
2
3

---

**Flashcard 40/40**

**Pregunta:**
What is the expected output of:
```python
try:
    raise Exception(42, 0, 13, 44, "code")
except Exception as e:
    print(len(e.args))
```

**Respuesta:**
5

---

Este formato está optimizado para Kindle 7" con:
- Texto grande y legible
- Diseño simple de una pregunta por tarjeta
- Sintaxis de código claramente formateada
- Espaciado adecuado para pantallas pequeñas
