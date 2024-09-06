class: center, middle

### Llenguatges de Programació

## Sessió 2: Python avançat

![:scale 60%](figures/python.svg)<br><br>

**Gerard Escudero i Albert Rubio**

![:scale 75%](figures/fib.png)

---
class: left, middle, inverse

## Contingut

- .cyan[Classes]

- Tipus algebraics

- *Lazyness*

- Clausures

- Decoradors

- Exercicis

---

# Classes I

Exemple de classe:

```python3
class Treballador:
    treCompt = 0                # atribut de classe: 
                                # un únic valor per classe
    def __init__(self, nom, salari):  # constructor
        self.nom = nom          # definició d'atribut  
        self.salari = salari    # self representa el objecte creat
        Treballador.treCompt += 1

    def getCompt(self):         # definició de mètode
        return Treballador.treCompt

    def getSalari(self):
        return self.salari
```

Exemple d'interacció:

```python3
tre1 = Treballador("Pep", 2000)
tre2 = Treballador("Joan", 2500)
tre1.getSalari()  👉  2000
tre1.salari  👉  2000 
tre1.getCompt()  👉  2
Treballador.treCompt  👉  2
```

---

# Classes II

Podem afegir, eliminar o modificar atributs de classes i objectes en qualsevol
moment:

```python3
tre1.edat = 8
tre1.edat  👉  8
hasattr(tre1, 'edat')  👉  True
del tre1.edat
hasattr(tre1, 'edat')  👉  False
```

La comanda `dir` ens retorna la llista d'atributs d'un objecte. Hi ha molts predefinits:
- `__dict__`, `__doc__`, `__name__`, `__module__`, `__bases__`.

### Atributs ocults

```python3
class Treballador:
    __treCompt = 0          # atribut ocult: començant per 2 _ 

tre1.__treCompt  ❌
tre1.tre1._Treballador__treCompt  👉  2
```

---

# Herència

Exemple:

```python3
class Fill(Treballador):    # pare entre ( )
    def fillMetode(self):
        print(’Cridem al metode del fill’)

tre3 = Fill('Manel', 1000)
tre3.fillMetode()
```

Podem tenir herència múltiple:

```python3
class A: # definim la classe A
.....
class B: # definim la calsse B
.....
class C(A, B): # subclasse de A i B
.....
```

Per fer comprovacions:

- `issubclass(sub, sup)`
- `isinstance(obj, Class)`

---
class: left, middle, inverse

## Contingut

- .brown[Classes]

- .cyan[Tipus algebraics]

- *Lazyness*

- Clausures

- Decoradors

- Exercicis

---

# Tipus enumerats

Donen la llista de valors possibles dels objectes:

**Pedra, paper, tisores:**

```python3
class Pedra:
    pass

class Paper:
    pass

class Tisores:
    pass

Jugada = Pedra | Paper | Tisores

guanya = lambda a, b: (a, b) in [(Paper,Pedra),(Pedra,Tisores),(Tisores,Paper)]

```

**Exemple:**

Guanya la primera a la segona?

```python3
guanya(Paper, Pedra)  👉  True
```

---

# Tipus algebraics 

Defineixen constructors amb zero o més dades associades:

```python3
from dataclasses import dataclass

@dataclass
class Rectangle:
    amplada: float
    alçada: float

@dataclass
class Quadrat:
    mida: float

@dataclass
class Cercle:
    radi: float

class Punt:
    pass

Forma = Rectangle | Quadrat | Cercle | Punt
```

- El decorador `dataclass` defineix automàticament mètodes com `__init__`.

---

# Funcions amb tipus algebraics

**Declaració:**

```python3
from math import pi

def area(f):
    match f:
        case Rectangle(amplada, alçada):
            return amplada * alçada
        case Quadrat(mida):
            return area(Rectangle(mida, mida))
        case Cercle(radi):
            return pi * radi**2
        case Punt():
            return 0
```

- `match` permet reconèixer patrons

**Crida:**

```python3
area(Quadrat(2.0))  👉  4.0
```

---

# Tipus recursius

**Arbre binari:**

.cols5050[
.col1[
```python3
from __future__ import annotations
from dataclasses import dataclass

class Buit:
    pass

@dataclass
class Node:
    val: int
    esq: Arbre
    dre: Arbre

Arbre = Node | Buit
```
]
.col2[
```python3
def mida(a: Arbre) -> int:
    match a:
        case Buit():
            return 0
        case Node(x, e, d):
            return 1 + mida(e) + mida(d)
```

```python3
t = Node(1,Node(2,Buit(),Buit()),
           Node(3,Buit(),Buit()))

mida(t)  👉  3
```
]]

- `annotations` permet els tipus recursius (en aquest cas `Arbre`).

---
class: left, middle, inverse

## Contingut

- .brown[Classes]

- .brown[Tipus algebraics]

- .cyan[*Lazyness*]

- Clausures

- Decoradors

- Exercicis

---

# Iteradors

En python existeixen mols tipus que són iterables: 
- strings, llistes, diccionaris i conjunts
- definits per l'usuari.

El protocol d'iteració el defineixen els mètodes:
- `__iter__` i `next`

i llença l'excepció `StopIteration` en acabar:

.col5050[
.col1[
```python3
s = 'abc'
for c in s:
    print(c)
👉
a
b
c
```
]
.col2[
```python3
s = 'abc'
it = iter(s)
while True:
    try:
        print(it.__next__())
    except StopIteration:
        break
```
]]


---

# Generadors I

Són el mecanisme que permeten l'avaluació *lazy* en python3.

Exemple: sèrie de fibonacci fins a un nombre determinat.

.col5050[
.col1[
```python3
def fib(n):
    a = 0
    yield a
    b = 1
    while True:
        if b <= n:
            yield b
            a, b = b, a + b
        else:
            raise StopIteration
```
]
.col2[
```python3
f = fib(1)
next(f)  👉  0
next(f)  👉  1
next(f)  👉  1
next(f)  ❌  StopIteration

## La comanda yield para l'execució 
## de la funció fins a la següent 
## invocació de next.


## amb list comprehension
[x for x in fib(25)]
👉
[0, 1, 1, 2, 3, 5, 8, 13, 21]
```
]
]
 
---

# Generadors II

Els generadors poden ser infinits:

```python3
def fib2():
    a = 0
    yield a
    b = 1
    while True:
        yield b
        a, b = b, a + b
```

```python3
f = fib2()
[next(f) for _ in range(8)]
👉
[0, 1, 1, 2, 3, 5, 8, 13]
```

---

# Generadors III

.cols5050[
.col1[
classe amb generador:
```python3
class fib:
    def \_\_iter\_\_(self):
        a, b = 0, 1
        while True:
            yield b
            a, b = b, a + b
```

```python3
for (i, x) in enumerate(fib(), 1):
    if i > 10:
        break
    print(i, x)
👉
1 1
2 1
3 2
4 3
5 5
6 8
```
]
.col2[
classe amb generador i iterador:
```python3
class fib2:
    def \_\_init\_\_(self):
        self.gen = self.\_\_iter\_\_()
```
```python3
    def \_\_next\_\_(self):
        return next(self.gen)
```
```python3
    def \_\_iter\_\_(self):
        a, b = 0, 1
        while True:
            yield b
            a, b = b, a + b
```
```python3
f = fib2()
print([next(f) for \_ in range(6)])
👉  [1, 1, 2, 3, 5, 8]
```
]]
Són útils quan volem tenir varies instàncies del generador funcionant a l'hora.

---
class: left, middle, inverse

## Contingut

- .brown[Classes]

- .brown[Tipus algebraics]

- .brown[*Lazyness*]

- .cyan[Clausures]

- Decoradors

- Exercicis

---

# Memorització amb valors per defecte

Aquesta característica ens permet fer programació dinàmica fàcilment:

### Fibonacci

.col5050[
.col1[
#### Versió recursiva:

```python3
def fib(n):
    if n in [0, 1]:
        return n
    return fib(n-1) + fib(n-2)
```

```python3
test(fib, 40)
👉
f(40) = 102334155
temps(s): 30.437519
```
]
.col2[
#### Programació dinàmica:

```python3
def efib (n, mem={0:0, 1:1}):
    if n not in mem:
        mem[n] = efib(n-1) + efib(n-2)
    return mem[n]
```

```python3
test(efib, 40)
👉
f(40) = 102334155
temps(s): 0.000059
```
]
]

---

# Funcions niuades

Python3 accepta funcions niuades.

Un exemple és la funció `test` de l'exemple anterior. Conté una funció `prec` a dins seu.

```python3
from pytictoc import TicToc

def test(f, n):
    def prec(x):
        return '{:.6f}'.format(x)

    t = TicToc()
    t.tic()
    print('f(', n,') = ', f(n), sep='')
    print('temps(s):', prec(t.tocvalue()))
```

---

# Memorització amb funcions niuades

La solució passa per definir un diccionari i una funció imbricada:

```python3
def efib2(x):
    mem = {0:0, 1:1}       # la memòria

    def mfib(n):
        if n not in mem: 
            mem[n] = mfib(n-1) + mfib(n-2)
        return mem[n]

    return mfib(x)
```

```python3
test(efib2, 40)
👉
f(40) = 102334155
temps(s): 0.000036
```


---

# Clausures

Una clausura (*closure*) és una mena funció *callback*. 

```python3
def test(n):
    def prec(x):
        return '{:.6f}'.format(x)

    def clausura(f):
        t = TicToc()
        t.tic();
        print('f(', n,') = ', f(n), sep='')
        print('temps(s):', prec(t.tocvalue()))

    return clausura
```

```python3
test40 = test(40)
test40(efib)
👉
f(40) = 102334155
temps(s): 0.000036

```

S'utilitzen per amagar dades (*data hiding*) i evitar així les variables globals.

---

# Memorització genèrica

Podem fer-ho amb una funció d'ordre superior o amb classes.

```python3
def memoritza (f):
    # Això es pot fer perquè els diccionaris són mutables.
    mem = {}       # la memòria

    def f2 (x):
        if x not in mem:
            mem[x] = f(x)
        return mem[x]
    return f2

def fib(n):
    if n in [0, 1]:
        return n
    return fib(n-1) + fib(n-2)
```

```python3
# Com que la funció és recursiva hem de redefinir la funció
test40 = test(40)
fib = memoritza(fib)
test40(fib)
👉
f(40) = 102334155
temps(s): 0.000051
```

---
class: left, middle, inverse

## Contingut

- .brown[Classes]

- .brown[Tipus algebraics]

- .brown[*Lazyness*]

- .brown[Clausures]

- .cyan[Decoradors]

- Exercicis


---

# Decoradors

Són un métode per alterar quelcom invocable (*callable*).

Ho podem fer mitjançant les clausures.

.col5050[
.col1[
```python3
def testDec(f):
    def wrapper(*args):
        valor = f(*args)
        print('fib(' + str(args[0]) + ') = ' + \
              str(valor))
        return valor

    return wrapper

@testDec
def efib (n, mem={0:0,1:1}):
    if n not in mem:
        mem[n] = efib (n-1) + efib (n-2)
    return mem[n]
```
]
.col2[
```python3
test4 = test(4)
test4(efib)
👉
fib(1) = 1
fib(0) = 0
fib(2) = 1
fib(1) = 1
fib(3) = 2
fib(2) = 1
fib(4) = 3
f(4) = 3
temps(s): 0.000035
```
]
]

---

# Decoradors parametritzats

Podem afegir arguments parametritzant els decoradors:

.col5050[
.col1[
```python3
def testInterval(inici, fi):
    def decorador(f):
        def wrapper(*args):
            valor = f(*args)
            n = args[0]
            if inici <= n <= fi:
                print('fib(' + str(n) + ') = ' + \
                      str(valor))
            return valor

        return wrapper
    return decorador

@testInterval(35, 40)
def efib (n, mem={0:0,1:1}):
    if n not in mem:
        mem[n] = efib (n-1) + efib (n-2)
    return mem[n]
```
]
.col2[
```python3
test40 = test(40)
test40(efib)
👉
fib(35) = 9227465
fib(36) = 14930352
fib(35) = 9227465
fib(37) = 24157817
fib(36) = 14930352
fib(38) = 39088169
fib(37) = 24157817
fib(39) = 63245986
fib(38) = 39088169
fib(40) = 102334155
f(40) = 102334155
temps(s): 0.000078
```
]
]

---

# Memorització genèrica amb decoradors

```python3
def memoritza (f):
    mem = {}
    def f2 (x):
        if x not in mem:
            mem[x] = f(x)
        return mem[x]
    return f2

@memoritza
def fib(n):
    if n in [0, 1]:
        return n
    return fib(n-1) + fib(n-2)
```

---
class: left, middle, inverse

## Contingut

- .brown[Classes]

- .brown[Tipus algebraics]

- .brown[*Lazyness*]

- .brown[Clausures]

- .brown[Decoradors]

- .cyan[Exercicis]


---

# Exercicis

* Feu aquests problemes de Jutge.org:

  - [P71608](https://jutge.org/problems/P71608_ca) Classe per arbres 

  - [P45231](https://jutge.org/problems/P45231_ca) Generadors

  - [P53498](https://jutge.org/problems/P53498_ca) Definició d'un iterable
