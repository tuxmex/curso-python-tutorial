Tienes razón, voy a crear las flashcards completas con código y explicación en formato optimizado para Kindle 7":

---

**Flashcard 1/40**

**Pregunta:**
```python
from random import randint
for i in range(2):
    print(randint(3,4), end='')
```

**Respuesta:**
**Posibles salidas:** 33, 34, 43, 44

**Explicación:**
- `randint(3,4)` genera 3 o 4 aleatoriamente
- Se ejecuta 2 veces en el loop
- `end=''` evita salto de línea
- Todas las combinaciones son posibles

---

**Flashcard 2/40**

**Pregunta:**
```python
s = "this is a string"
print(s[2:8])
```

**Respuesta:**
`is is`

**Explicación:**
- Slice `[2:8]` toma desde índice 2 hasta 7
- Índice 2: 'i' de "this"
- Índice 7: espacio antes de "a"
- Resultado: "is is " (incluye espacios)

---

**Flashcard 3/40**

**Pregunta:**
Importar constante matemática **e** desde **math**

**Respuesta:**
```python
from math import e
```

**Explicación:**
- `from module import name` importa específicamente
- `e` es constante matemática ≈ 2.71828
- Se usa directamente sin prefijo `math.`

---

**Flashcard 4/40**

**Pregunta:**
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
```
0
1
2
```

**Explicación:**
- **Closures**: cada función recuerda su `num`
- `outer_func(i)` crea closure con valor actual de `i`
- Las funciones se ejecutan después con sus valores preservados

---

**Flashcard 5/40**

**Pregunta:**
```python
numbers = [1,2,3,4,5,6,7,8,9,10]
divisor = 3
pairs = [(numbers[i], numbers[j]) 
         for i in range(len(numbers)) 
         for j in range(i+1, len(numbers)) 
         if (numbers[i] + numbers[j]) % divisor == 0]
print(pairs)
```

**Respuesta:**
`[(1,2), (1,5), (1,8), (2,4), (2,7), (2,10), (3,6), (3,9), (4,5), (4,8), (5,7), (5,10), (6,9), (7,8), (8,10)]`

**Explicación:**
- Encuentra pares únicos donde la suma es divisible por 3
- `j > i` evita duplicados como (1,2) y (2,1)
- 15 pares cumplen la condición

---

**Flashcard 6/40**

**Pregunta:**
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
```
False
True
False
True
```

**Explicación:**
- Instancias NO tienen `__name__` ni `__bases__`
- Instancias SÍ tienen `__module__`
- Clases SÍ tienen `__name__`

---

**Flashcard 7/40**

**Pregunta:**
```python
class Animal:
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def __init__(self, breed):
        self.breed = breed

fido = Dog("Golden Retriever")
# ¿Tipo de fido?
```

**Respuesta:**
`Dog`

**Explicación:**
- `fido` es instancia de `Dog`
- `type(fido)` devuelve `Dog`
- Herencia no cambia el tipo de instancia

---

**Flashcard 8/40**

**Pregunta:**
```python
with open('file.txt', 'w') as f:
    f.write('Hello world!')

with open('file.txt', 'r') as f:
    data = f.read()

with open('file.txt', 'wb') as f:
    f.write(data.encode())

with open('file.txt', 'rb') as f:
    data = f.read()

print(data)
```

**Respuesta:**
`b'Hello world!'`

**Explicación:**
- Primero escribe como texto
- Lee como texto
- Escribe como bytes (codificado)
- Lee como bytes
- Salida final es objeto bytes

---

**Flashcard 9/40**

**Pregunta:**
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
`code2Upro2U`

**Explicación:**
- `f(42)`: sin error → ejecuta `else` + `finally`
- `f(0)`: ZeroDivisionError → ejecuta `except` + `finally`
- `end=''` mantiene todo en una línea

---

**Flashcard 10/40**

**Pregunta:**
Operadores válidos para strings (2 respuestas)

**Respuesta:**
`*` y `*=`

**Explicación:**
- `*`: repetición → `"a" * 3 = "aaa"`
- `*=`: repetición in-place → `s *= 2`
- `/` y `-` NO son válidos para strings

---

**Flashcard 11/40**

**Pregunta:**
```python
class MyClass:
    __private_var = 10
    
    def get_private_var(self):
        return self.__private_var
    
    def set_private_var(self, value):
        self.__private_var = value

a = MyClass()
a.set_private_var(20)
print(a.get_private_var())
```

**Respuesta:**
`20`

**Explicación:**
- Variables con `__` son "privadas" pero accesibles
- Name mangling: `_MyClass__private_var`
- Métodos públicos pueden modificarlas

---

**Flashcard 12/40**

**Pregunta:**
```python
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transpose = [[row[i] for row in matrix] 
             for i in range(len(matrix[0]))]
print(transpose)
```

**Respuesta:**
`[[1,4,7], [2,5,8], [3,6,9]]`

**Explicación:**
- Transposición: filas → columnas
- List comprehension anidada
- `row[i]` toma elemento i-ésimo de cada fila

---

**Flashcard 13/40**

**Pregunta:**
```python
s = "a,b,c,d,e"
print(s.split(",")[::-1])
```

**Respuesta:**
`['e', 'd', 'c', 'b', 'a']`

**Explicación:**
- `split(",")` → `['a','b','c','d','e']`
- `[::-1]` revierte la lista
- Resultado: lista invertida

---

**Flashcard 14/40**

**Pregunta:**
```python
class A:
    def foo(self): print("A")
class B(A):
    def foo(self): print("B")
class C(A):
    def foo(self): print("C")
class D(B, C):
    pass

obj = D()
obj.foo()
```

**Respuesta:**
`B`

**Explicación:**
- **MRO (Method Resolution Order)**: D → B → C → A
- Python usa depth-first, left-to-right
- `B` tiene prioridad sobre `C`

---

**Flashcard 15/40**

**Pregunta:**
```python
s = "ProCoding"
print(sorted(s, reverse=True))
```

**Respuesta:**
`['r','o','o','n','i','g','d','P','C']`

**Explicación:**
- `sorted()` ordena caracteres
- `reverse=True` orden descendente
- Mayúsculas antes que minúsculas en ASCII

---

**Flashcard 16/40**

**Pregunta:**
¿Dónde guarda Python los archivos .pyc al importar?

**Respuesta:**
`__pycache__`

**Explicación:**
- Directorio para bytecode compilado
- Acelera imports posteriores
- Nombre: `modulo.cpython-XX.pyc`

---

**Flashcard 17/40**

**Pregunta:**
```python
nums1 = [1,2,3]
nums2 = [4,5,6]
result = [[num1 * num2 for num1 in nums1] 
          for num2 in nums2]
print(result)
```

**Respuesta:**
`[[4,8,12], [5,10,15], [6,12,18]]`

**Explicación:**
- Producto de cada elemento de nums2 con todos los nums1
- Lista externa: por cada num2
- Lista interna: num2 * cada num1

---

**Flashcard 18/40**

**Pregunta:**
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
`4 6`

**Explicación:**
- Inicial: x=2, y=3
- `multiply(2)`: x=2*2=4, y=3*2=6
- Modifica atributos directamente

---

**Flashcard 19/40**

**Pregunta:**
¿Qué códigos imprimen `True`? (2 respuestas)

**Respuesta:**
```python
print("" < "Z")
print("20" < "8")
```

**Explicación:**
- `"" < "Z"`: string vacío < cualquier string
- `"20" < "8"`: comparación lexicográfica, '2' < '8'

---

**Flashcard 20/40**

**Pregunta:**
¿Qué hace `pip list` en la línea de comandos?

**Respuesta:**
Lista todos los paquetes instalados en el entorno actual

**Explicación:**
- Muestra nombre y versión
- No lista paquetes disponibles en PyPI
- Útil para verificar instalaciones

---

**Flashcard 21/40**

**Pregunta:**
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
`('list index out of range',)`

**Explicación:**
- `data[-4]` fuera de rango (solo 3 elementos)
- Se captura excepción
- `exception.args` contiene tupla con mensaje

---

**Flashcard 22/40**

**Pregunta:**
```python
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        self.__salary = salary

e = Employee("Alice", 50000)
e.set_salary(-1000)
```

**Respuesta:**
El programa termina con error

**Explicación:**
- `set_salary(-1000)` lanza ValueError
- No se captura la excepción
- Programa termina abruptamente

---

**Flashcard 23/40**

**Pregunta:**
```python
try:
    print(42/"0")
except:
    print("something went wrong...")
except (ValueError):
    print("value error")
except (ZeroDivisionError):
    print("zero division error")
```

**Respuesta:**
El código es erróneo

**Explicación:**
- `except` sin tipo debe ser el último
- SyntaxError: se detecta en tiempo de compilación

---

**Flashcard 24/40**

**Pregunta:**
¿Cuál es verdadero sobre bloques try?

**Respuesta:**
Un bloque try puede tener cláusula finally sin except

**Explicación:**
- Sintaxis válida: `try: ... finally: ...`
- `finally` siempre se ejecuta
- No es obligatorio tener `except`

---

**Flashcard 25/40**

**Pregunta:**
```python
class Person:
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    name = property(get_name, set_name)

p = Person("John")
p.name = "Bob"
print(p.get_name())
```

**Respuesta:**
`Bob`

**Explicación:**
- `property` crea atributo gestionado
- `p.name = "Bob"` llama a `set_name`
- `get_name()` devuelve valor actualizado

---

**Flashcard 26/40**

**Pregunta:**
```python
class MyClass:
    class_var = 0
    
    def __init__(self, instance_var):
        self.instance_var = instance_var

a = MyClass(5)
b = MyClass(10)
a.class_var += 1
print(a.class_var + b.class_var)
```

**Respuesta:**
`1`

**Explicación:**
- `a.class_var += 1` crea atributo de instancia
- No modifica la variable de clase
- `a.class_var = 1`, `b.class_var = 0`

---

**Flashcard 27/40**

**Pregunta:**
```python
class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg

raise MyException("This is a custom exception")
```

**Respuesta:**
`MyException: This is a custom exception`

**Explicación:**
- Creación de excepción personalizada
- `raise` lanza la excepción
- Mensaje incluido en la salida

---

**Flashcard 28/40**

**Pregunta:**
¿Cómo actualizar paquetes con pip? (2 respuestas)

**Respuesta:**
`pip install --upgrade package`
`pip install -U package`

**Explicación:**
- Ambas opciones son equivalentes
- Descarga e instala última versión
- No existe comando `reinstall`

---

**Flashcard 29/40**

**Pregunta:**
```python
try:
    x = input("Enter x: ")  # "procoding"
    a = len(x)              # 9
    y = input("Enter y: ")  # ""
    b = len(y) * 2          # 0
    print(a/b)              # 9/0
except ZeroDivisionError:
    print("Zero!")
```

**Respuesta:**
`Zero!`

**Explicación:**
- `len("") = 0` → `b = 0`
- `9/0` → ZeroDivisionError
- Se captura y imprime "Zero!"

---

**Flashcard 30/40**

**Pregunta:**
```python
class A:
    var_a = 10
    def fun_a(self): return 11

class B:
    var_b = 20  
    def fun_b(self): return 21

class Sub(A, B):
    pass

obj = Sub()
print(obj.var_a, obj.fun_b())
```

**Respuesta:**
`10 21`

**Explicación:**
- Herencia múltiple
- `obj.var_a` de clase A
- `obj.fun_b()` de clase B

---

**Flashcard 31/40**

**Pregunta:**
```python
data = bytearray(b"Hello, world!")
with open("file.txt", "w") as f:
    f.write(data)
```

**Respuesta:**
TypeError

**Explicación:**
- Modo "w" espera string, no bytearray
- Necesita `data.decode()` para convertir a string
- TypeError en tiempo de ejecución

---

**Flashcard 32/40**

**Pregunta:**
```python
class Book:
    def __str__(self): 
        return f"{self.title} by {self.author}"

class Ebook(Book):
    def __str__(self):
        return f"{super().__str__()} [{self.file_format}]"

book1 = Book("Catcher", "Salinger")
book2 = Ebook("Mockingbird", "Lee", "PDF")
print(book1)
print(book2)
```

**Respuesta:**
```
Catcher by Salinger
Mockingbird by Lee [PDF]
```

**Explicación:**
- `__str__` para representación legible
- `super()` llama al método del padre
- Herencia y polimorfismo

---

**Flashcard 33/40**

**Pregunta:**
```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    
    def get_balance(self):
        return self._balance
    
    def __str__(self):
        return f"The balance is {self.get_balance()}"

b = BankAccount(100)
print(b)
```

**Respuesta:**
`The balance is 100`

**Explicación:**
- `print(b)` llama automáticamente a `__str__`
- `__str__` llama a `get_balance()`
- Output formateado

---

**Flashcard 34/40**

**Pregunta:**
```python
print("a" > "")      # True
print("8" > "10")    # True  
print("Mark" > "MARK") # True
```

**Respuesta:**
`True True True`

**Explicación:**
- `"a" > ""`: cualquier string > string vacío
- `"8" > "10"`: '8' > '1' (comparación carácter por carácter)
- `"Mark" > "MARK"`: minúsculas > mayúsculas en ASCII

---

**Flashcard 35/40**

**Pregunta:**
Diferencia entre `find()` e `index()` (2 respuestas)

**Respuesta:**
- `find()` devuelve -1 si no encuentra
- `index()` lanza ValueError si no encuentra
- Un codepoint es número que corresponde a carácter

**Explicación:**
- Ambos buscan substrings
- Comportamiento diferente en caso de no encontrar
- Codepoint: representación numérica en Unicode

---

**Flashcard 36/40**

**Pregunta:**
¿Verdadero sobre constructores en Python?

**Respuesta:**
`__init__` declara el constructor y se invoca automáticamente al crear objeto

**Explicación:**
- `__init__` es el método constructor
- Se llama automáticamente con `ClassName()`
- No hay keyword `new` como en otros lenguajes

---

**Flashcard 37/40**

**Pregunta:**
```python
try:
    with open("file.txt", "r") as f:
        f.write("Hello, world!")
except IOError as e:
    print("Permission denied")
```

**Respuesta:**
`Permission denied`

**Explicación:**
- Modo "r" es solo lectura
- `write()` en archivo readonly → IOError
- Se captura y muestra mensaje

---

**Flashcard 38/40**

**Pregunta:**
```python
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def add_value(self, x):
        self.value += x

a = MyClass(5)
b = a          # Misma referencia
b.add_value(10)
print(a.value + b.value)
```

**Respuesta:**
`30`

**Explicación:**
- `a` y `b` referencian el mismo objeto
- `b.add_value(10)` modifica `a.value` también
- `a.value = 15`, `b.value = 15` → suma = 30

---

**Flashcard 39/40**

**Pregunta:**
```python
def func1():
    class Holder:
        x = 1
    h = Holder()
    
    def func2():
        h.x += 1
        print(h.x)
    
    func2()
    func2()

func1()
```

**Respuesta:**
```
2
3
```

**Explicación:**
- `func2` es closure que accede a `h`
- `h.x` se modifica entre llamadas
- Estado preservado a través de llamadas

---

**Flashcard 40/40**

**Pregunta:**
```python
try:
    raise Exception(42, 0, 13, 44, "code")
except Exception as e:
    print(len(e.args))
```

**Respuesta:**
`5`

**Explicación:**
- `Exception` puede recibir múltiples argumentos
- `e.args` es tupla con los argumentos
- `len(e.args)` cuenta cuántos argumentos hay

---

Este formato incluye:
- ✅ Código completo en cada flashcard
- ✅ Explicación detallada
- ✅ Texto optimizado para Kindle 7"
- ✅ Sintaxis Python formateada correctamente
- ✅ 40 flashcards numeradas
