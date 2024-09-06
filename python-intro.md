class: center, middle

### Llenguatges de Programació

## Sessió 1: Python bàsic i funcional

![:scale 60%](figures/python.svg)<br><br>

**Gerard Escudero i Albert Rubio**

![:scale 75%](figures/fib.png)

---
class: left, middle, inverse

## Contingut

- .cyan[Elements bàsics]

- Iterables

- Part funcional

- Exercicis

---

# Introducció

.cols5050[
.col1[
#### Paradigmes:

  - imperatiu,

  - orientat a objectes,

  - funcional.
]
.col2[
#### Característiques:

  - interpretat,

  - llegibilitat,

  - *lazyness*.
]]

Té una gran quantitat de llibreries disponibles.

---

# Entorns

### 'Hello world!'

```python3
print('Hello world!')
```

```python3
nom = input('Com et dius? ')
print('Hola', nom + '!')
```

### Línia de comandes: 

`python3 script.py`

### *idle* : entorn Python 3 

`idle` o `idle3`

### Codificació:

Utilitza 'utf-8'

---

# Blocs i comentaris

### Comentaris

```python3
# això és un comentari
```

### Blocs

Els blocs (*suites*) es marquen per l'identació. 

```python3
if condicio:
    print('ok!')
```

L'estil estàndard *PEP8* es marcar-ho amb 4 espais.

### Línies llarges

Podem tallar línies amb `\`:
```python3
total = x*100 + \
        y*10
```

---

# Variables i assignació

Declaració implícita (valor): 
```python3
a = 2
```

Assignació:
```python3
x = y = z = 0
x, y, z = 0, 5, "Llenguatges"
x, y = y, x
```

Assignació augmentada:
```python3
a += 3
```

⚠️ No té ni `--` ni `++`!


---

# Tipus estàndard

### Nombres

`int`, `float`, `complex`

Són tipus i funcions de conversió.

`int` no té rang. Pot tractar nombres arbitrariàment llargs.

Operadors usuals excepte: `**` (potència) i `//` (divisió entera)

.col5050[
.col1[
### Booleans

`True`, `False`

Operadors: `and`, `or`, `not`
]
.col2[
### Funcions de tipus
```python3
type(3)  👉  int 

isinstance(3, int)  👉  True

isinstance(3, (float, bool))  👉  False 

```
]]

---

# Condicionals

### Acció (*statement* ):

```python3
if x < 0:
    signe = -1
elif x > 0:
    signe = 1
else:
    signe = 0
```
Els `else` i `elif` són opcionals.

### Expressió:
```python3
x = 'parell' if 5 % 2 == 0 else 'senar'
```

---

# Iteracions

Taula de multiplicar:

### while

```python3
n, i = int(input('n? ')), 1
while i <= 10:
    print(n, 'x', i, '=', n * i)
    i += 1
```

### for

```python3
n = int(input('n? '))
for i in range(1, 11):
    print(n, 'x', i, '=', n * i)
```

El `for` funciona sobre tipus *iterables*.

També podem usar el `break` i el `continue`, amb la semàntica usual sobre tots dos bucles.


---

# Funcions I

Declaració:

```python3
def primer(n):
    for d in range(2, n // 2 + 1):
        if n % d == 0:
            return False
    return True
```

Crida:

```python3
primer(5)  👉  True
```

### Retorn de múltiples valors:

```python3
def divisio(a, b):
    return a // b, a % b

x, y = divisio(7, 2)  # x 👉 3, y 👉 1
```
Quan tornem més d'un valor ho fa internament en forma de *tupla*.

---

# Funcions II

### Valors per defecte:

```python3
from string import punctuation

def remPunc(s, tl=True):
    rt = ''
    for c in s.lower() if tl else s:
        if c not in punctuation:
            rt = rt + c
    return rt

remPunc('Hola, sóc un exemple!')
👉  'hola sóc un exemple'

remPunc('Hola, sóc un exemple!', tl=False)
👉  'Hola sóc un exemple'
```

---
class: left, middle, inverse

## Contingut

- .brown[Elements bàsics]

- .cyan[Iterables]

- Part funcional

- Exercicis

---

# Strings I

Tipus `str`.

Els *strings* són iterables.

### Operacions:
```python3
z = 'Llenguatges'

z[2]    👉  'e'        # posició 

z[3:6]  👉  'ngu'      # subcadena 

z[:4]   👉  'Llen'     # prefix 

z[8:]   👉  'ges'      # sufix 

z + ' Programació'   👉  'Llenguatges Programació'   # concatenar 

z * 3   👉  'LlenguatgesLlenguatgesLlenguatges'      # repetir 

len(z)  👉  11         # mida
```

---

# Strings II

### Altres operacions i mètodes

```python3
z = 'Llenguatges'

'ng' in z  👉  True 

'ng' not in z  👉  False

z.find('ng')  👉  3               # cerca i torna posició

z.count('e')  👉  2               # comptar  

'Hello world!\n'.strip()  👉  'Hello world!'   # treu el \n

'1,2,3'.split(',')  👉  ['1', '2', '3']    # parteix un string

','.join(['1', '2', '3'])  👉  '1,2,3'     # operació inversa
```

Els *strings* són *immutables*:

```python3
z[0] = 'l'  ❌   # TypeError: 'str' object does not support item assignment
```

---

# Llistes

Les llistes (`list`) són heterogènies:
```python3
z = ["hola",5,"llenguatge",6.63,2]
```

Tenen les mateixes operacions que els *strings* i també són *iterables*.

Per recorrer dos o més iterables podem utilitzar el `zip`:
```python3
def prodEscalar(v, w):
    res = 0
    for x, y in zip(v, w):
        res += x * y
    return res
```

Altres operacions predefinides de la classe `list`:

- `append`, `count`, `pop`, etc.

---

# Tuples

Les tuples (`tuple`) són:

- com les llistes
- *immutables* (de només de lectura)

```python3
z = ("hola",5,"llenguatge",6.63,2)
z = (5,)      # tupla d'un sol element
              # (5) és l'enter 5
```

# Conjunts

Els conjunts (`set`) admeten les operacions: 

- `len`, `in`, `not in`, issubset (`<=`), issuperset (`>=`),
- union (`|`), intersection (`&`), difference (`-`),
- `add`, `remove` ...

---

# Diccionaris

Els diccionaris (`dict`):

- contenen parells clau-valor 
- permeten accés directe

```python3
dic = {}                   # diccionari buit
dic["prim"] = "el primer"  # afegir o actualitzar un element
del(dic['prim`])           # esborrar-lo 
dic = {"nom": "albert","num":37899, "dept": "computer science"} 
                           # inicialitzar-lo amb dades
```

Els diccionaris són iterables (en iterar amb el for recorrem les claus):
```python3
def suma(d):
    s = 0
    for k in d:
        s += d[k]
    return s

suma({'a': 1, 'b': 2})  👉  3
```

---
class: left, middle, inverse

## Contingut

- .brown[Elements bàsics]

- .brown[Iterables]

- .cyan[Part funcional]

- Exercicis

---

# Funcions anònimes

Les funcions són un tipus intern en python (*function*). Poden ser tractades com a dades i, per tant, com a paràmetres d'una funció.

Disposem de funcions anònimes tipus *lambda*:
```python3
lambda parametres: expressió
```
on els `parametres` són zero o més paràmetres separats per comes.

```python3
doble = lambda x: 2 * x      # una altra forma de definir funcions

doble(3)  👉  6

type(doble)  👉  <class 'function'>
```

Una aplicació pràctica és el paràmetre `key` de les funcions `max`, `min` i `sort`:

```python3
d = {'a': 2, 'b': 1}

max(d, key = lambda x: d[x])  👉  'a'      # clau amb valor màxim d'un diccionari
```

---

# Funcions d'ordre superior I

### map
`map(funció, iterable)  👉  generador`: aplica la funció a cadascun dels elements de l'iterable.
```python3
list(map(lambda x: x * 2, [1, 2, 3]))  👉  [2, 4, 6]
```

### filter
`filter(funció, iterable)  👉  generador`: és el subiterable amb els elements que fan certa la funció booleana.
```python3
mg3 = lambda x: x > 3

list(filter(mg3, [3, 6, 8, 1]))  👉  [6, 8]
```

---

# Funcions d'ordre superior II

### reduce (fold)
`reduce(funció, iterable[, valor_inicial])  👉  valor`: desplega una funció per l'esquerra.
```python3
from functools import reduce

reduce(lambda acc,y: acc+y, [3,6,8,1])  👉  18

reduce(lambda acc,y: acc+y, [3,6,8,1], 0)  👉  18
```

---

# Llistes per comprensió I

### amb llistes

`[expressió for variable in iterable if expressió]`
```python3
[x ** 2 for x in range(4)]  👉  [0, 1, 4, 9]

[x for x in [0, 1, 4, 9] if x % 2 == 0]  👉  [0, 4]

[(x, y) for x in [1, 2] for y in 'ab']
👉  [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

### amb conjunts
```python3
{x for x in range(4) if x % 2 == 0}
👉  {0, 2}
```

---

# Llistes per comprensió II

### amb diccionaris
```python3
{x: x % 2 == 0 for x in range(4)}
👉  {0: True, 1: False, 2: True, 3: False}
```

### amb generadors

```python3
from itertools import count      # count és un generador infinit

g = (x**2 for x in count(1))     # g és un generador
                                 # dels quadrats dels naturals

next(g)  👉  1

[next(g) for _ in range(4)]  👉  [4, 9, 16, 25]
```
---

# Mòdul *operator*

La llibreria *operator* conté tots els operadors estàndard en forma de funcions, per a ser usades en funcions d'ordre superior.

```python3
from operator import mul
from functools import reduce

factorial = lambda n: reduce(mul, range(1, n+1))

factorial(5)  👉  120
```

Alguns exemples de funcions que conté són:

- `iadd(a, b)`: equivalent a `a += b`

- `attrgetter(attr)`:
```python3
f = attrgetter('name')
f(b)  👉  b.name
```

---

# Mòdul *itertools*

Aquesta llibreria conté moltes funcions relacionades amb les iteracions.

Té moltes funcions equivalents a Haskell:
```python3
from operator import mul
from itertools import accumulate

factorials = lambda n: accumulate(range(1, n + 1), mul)

[x for x in factorials(5)]  👉  [1, 2, 6, 24, 120]
```

Altres funcions amb equivalents Haskell són: `dropwhile`, `islice` (`take`),`repeat` o `takewhile`.

Té algunes funcions que fan d'iteradors combinatòrics: `product`, `permutations`, `combinations` o `combinations_with_replacement`.

És interessant fer un repàs a la documentacio d'aquesta llibreria:
https://docs.python.org/3.7/library/itertools.html

---
class: left, middle, inverse

## Contingut

- .brown[Elements bàsics]

- .brown[Iterables]

- .brown[Part funcional]

- .cyan[Exercicis]

---

# Exercicis

* Feu aquests problemes de Jutge.org:

  - [P84591](https://jutge.org/problems/P84591_ca) Funcions amb nombres

  - [P51956](https://jutge.org/problems/P51956_ca) Funcions amb llistes

  - [P80049](https://jutge.org/problems/P80049_ca) Ús d'iterables

  - [P66679](https://jutge.org/problems/P66679_ca) Llistes per comprensió

  - [P73993](https://jutge.org/problems/P73993_ca) Funcions d'ordre superior


