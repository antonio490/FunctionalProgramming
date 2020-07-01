
# Unpacking iterators by assigning to multiple variables

## Extended iterator unpacking using the *rest syntax

animals = 'Praying Mantils', 'Ant', 'Whale', 'Lizard'

# Multiple asignment
a1, a2, a3, a4 = animals
print(a1, a2, a3, a4)

animals_by_class = {'Praying Mantils', 'Ant'}, 'Whale', 'Lizard'
(a1, a2), a3, a4 = animals_by_class

a1, *rest, a2 = animals
print(a1, rest, a2)
'Praying Mantils', ['Ant', 'Whale'], 'Lizard'

## Unpacking a dict

animals_and_classes = {
    'Praying Matils' : 'Insect',
    'Ant'            : 'Insect',
    'Whale'          : 'Mammal',
    'Lizard'         : 'Reptile',
}

# Only get the keys
a1, a2, a3, a4 = animals_and_classes

(k1, v1), (k2, v2), (k3, v3), (k4, v4) = animals_and_classes

keys, values = animals_and_classes.keys(), animals_and_classes.values()

# Iterators

## Iterators are object that we can use in a 'for' loop
## Iterators not necessarily have a lenght or support indexing.
## Lists , Dicts and Tuples are sequences that extend the iterator protocol.

t = 'a', 'b', 'c'

for a in t:
    print(a)

# iter(), next() and StopIteration()

i = iter(t)
print(next(i)) # prints a

i = iter(t)
while True:
    try:
        e - next(i)
    except StopIteration
        break
    print(e)


# Creating our own iterator

## An iterator is an object with at least the following methods.
## _iter__() returns the actual object that will be iterated through.
## _next__() return the next element and raises a StopIterator when the iterator is exhausted.

import random

class RandomIterator:

    def __init__(self, *elements):

        self._elements = list(elements)

    def __iter__(self):
        
        random.shuffle(self._elements)
        self._cursor = 0
        return self

    def __next__(self):

        if self._cursor >= len(self._elements):
            raise StopIteration()
        e = self._elements[self._cursor]
        self._cursor += 1
        return e

i = RandomIterator(1, 2, 3)

for e in i:
    print(e)

