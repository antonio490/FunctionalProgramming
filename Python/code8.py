
# List and Dickt comprehensions and generator expressions

## List comprehensions

## Statements are instructions. Dont evaluate to something. Not used in (pure) functional programming.
## Expressions is something that evaluates to something. Expressions are use heavily on functional programming.

from math import sqrt

for i in range(5):
    print(sqrt(i))

## With list comprehension
[sqrt(i) for i in range(5)]

for i in range(5):
    if i%2:
        continue
    print(i)

## With list comprehension
[print(i) for i in range(5) if not i%2]


## Breaking with list comrpehensions

def fibonacci():

    yield 1
    yield 1
    l = [1, 1]
    while True:
        l = [l[-1], sum(l[-2:])]
        yield l[-1]

for i in fibonacci():
    if i > 10:
        break
    print(i)

## With list comprehension does not work.
[i for i in fibonacci() if i <= 10]

## Dict comprehensions

SPECIES = 'whale', 'grasshoper', 'lizard'
CLASS = 'mamal', 'insect', 'reptile'

d = dict(zip(SPECIES, CLASS))

d = {}
for species, class_ in zip(SPECIES, CLASS):
    d[species.capitalize()] = class_.capitalize()
print(d)

## Other way
d = {species.capitalize(): class_.capitalize() for species, class_ in zip(SPECIES, CLASS)}
print(d)

## Filtering dict comprehensions

d = {
    species.capitalize(): class_.capitalize()
    for species, class_ in zip(SPECIES, CLASS)
    if class_ != 'insect'
}

print(d)

## Generator expressions

from math import sqrt

g = (sqrt(i) for i in range(5))

## loop over or use next()
for i in g:
    print(i)

# Filtering
g = (i for i in range(10) if not i%2)
for i in g:
    print(i)

## Breaking generator
def fibonacci():

    yield 1
    yield 1
    l = [1, 1]
    while True:
        l = [l[-1], sum(l[-2:])]
        yield l[-1]


def stop():
    raise StopIteration()

g = (i for i in fibonacci() if i < 10 or stop())

for i in g:
    print(i)

## Other way

class EndGenerator(Exception): pass

def stop():
    raise EndGenerator()

def wrap():

    l =[]
    while True:
        try:
            l.append(next(g))
        except EndGenerator():
            break
    return l

g = wrap(i for i in fibonacci() if i < 10 or stop())
for i in g:
    print(i)


## Nested comprehensions

## Defining loop within loop
## When you need all combinations of the elements of two iterables
## Different from zip()

grid = []
for x in range(2):
    for y in range(2):
        grid.append([x,y])
    print(grid)

## FP way
def g(s):
    print(s)
    yield 1
    print(s)
    yield 2

grid = [ (x,y) for x in g('x') for y in g('y') ]
print(grid)


## Summary

# 1. Statements are instructions to the Python interpreter and expressions are things that evaluate to something.
# 2. Functional programming relies heavily on expressions
# 3. List and dict comprehensions support filtering and nesting but not breaking
# 4. Generator expressions are lazy list comprehensions.

