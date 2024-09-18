class: center, middle

### Llenguatges de Programació

## Interludi: aplicació vs composició

![:scale 40%](figures/haskell.png)<br><br>

**Gerard Escudero**

![:scale 75%](figures/fib.png)

---
class: left, middle, inverse

## Contingut

- .cyan[Aplicació vs composició]

- Notació *point-free*

- Exemple amb 2 paràmetres

---

# Aplicació vs composició

.cols5050[
.col1[
**Aplicació**:

```haskell
($) :: (a -> b) -> a -> b

-- ($) f x

--    f    $    x
-- funció     valor
```
]
.col2[
**Composició**:

```haskell
(.) :: (b -> c) -> (a -> b) -> a -> c

-- (.) f g x

--    f    .     g
-- funció     funció
```
]]

**Relació entre l'aplicació i la composició**:

```haskell
\x -> f (g x)  ≡  \x -> f $ g x  ≡  f . g
```

**Exemple**:

.cols5050[
.col1[
```haskell
appli2 f x = f $ f x

appli2 (*2) 2  👉  8
```
]
.col2[
```haskell
appli2 f = f . f

appli2 (*2) 2  👉  8
```
]]

---
class: left, middle, inverse

## Contingut

- .brown[Aplicació vs composició]

- .cyan[Notació *point-free*]

- Exemple amb 2 paràmetres

---

# Notació *Point-free*

Notació per definir funcions sense explicitar els paràmetres que porta la funció. Normalment les definim utilitzant la composició de funcions.

**Exemple**:

Definició d'un funció que, donada una llista, ens torni el número de parell que conté.

```haskell
numParells :: Integral a => [a] -> Int
numParells l = length (filter even l)
```

```haskell
-- Point-free
numParells :: Integral a => [a] -> Int
numParells = length . filter even
```

Les dues definicions són completament equivalents:

```haskell
numParells [1..5]  👉  2
```

---
class: left, middle, inverse

## Contingut

- .brown[Aplicació vs composició]

- .cyan[Notació *point-free*]

- Exemple amb 2 paràmetres

---

# Exemple amb 2 paràmetres

Definició d'un funció que, donada una llista i un enter, ens torni el número de vegades que apareix l'enter.

```haskell
numVegades :: Eq a => a -> [a] -> Int
numVegades x l = length $ filter (== x) l

numVegades 3 [3,2,3]  👉  2
```

```haskell
numVegades x l = (length . filter (== x)) l     -- canviem $ per .
```

```haskell
numVegades x = length . filter (== x)           -- treiem l
```

```haskell 
numVegades x =  length . (filter ((==) x)))     -- treiem x de (== x)
```

```haskell 
numVegades x =  length . (filter $ (==) x))     -- canviem () per $
```

```haskell 
numVegades x =  length . (filter . (==)) x      -- caviem  $ per .
```

---

# Exemple amb 2 paràmetres

En aquest punt tenim:

```haskell 
numVegades x =  length . (filter . (==)) x   -- necessitem quelcom com (f . g) x
```

Tenim els tipus simplificats i la `g`:

```haskell 
g :: Int -> [Int] -> [Int]
g = filter . (==)

numVegades :: Int -> [Int] -> Int
numVegades = f . g

(.) :: (b -> c) -> (a -> b) -> a -> c
a ≡ Int
b ≡ [Int] -> [Int]
c ≡ Int

length :: [Int] -> Int

f :: ([Int] -> [Int]) -> [Int] -> Int 
f ??? length???
```

---

# Exemple amb 2 paràmetres

**Solució**:

```haskell 
f :: ([Int] -> [Int]) -> [Int] -> Int 
f = (length .)
```


```haskell 
numVegades x = ((length .) . (filter . (==))) x       -- apliquem f . g
```

```haskell 
numVegades = ((length .) . (filter . (==)))           -- treiem x
```

**Test**:

.cols5050[
.col1[
```haskell 
numVegades = (length .) . 
             (filter . (==))

numVegades 3 [3,2,3]  👉  2
```
]
.col2[
```haskell 
f = (length .)
g = filter . (==)

(f . g) 3 [3,2,3]  👉  2
```
]]
