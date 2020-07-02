
# Functions that work with iterators

## Convenience functions
## zip(), map(), enumerate() and filter()

species_list = ['whale', 'lizard', 'Ant']
class_list = ['mammal', 'reptile', 'insect']
cuteness_list = [3, 2, 1, 0]

for i in range(len(species_list)):
    species = species_list[i]
    class_ = class_list[i]
    print("%s is a %s" % (species, class_))

for species, class_, cuteness in zip(species_list, class_list, cuteness_list):
    print("%s is a and has a cuteness rating of %d" %(species, class_, cuteness))

## Map()
## For each element on list we apply function sqrt
from math import sqrt

fibonacci = [1, 1, 2, 3, 5, 8]
for i in map(sqrt, fibonacci):
    print(i)

## Other way
for i in (sqrt(j) for j in fibonacci):
    print(i)

## Enumerate()
for i, species in enumerate(species_list):
    print(i, species)

## Other way
for i, species in ((i, species_list(i)) for i in range(len(species_list))):
    print(i, species)


## Filter()

for i in fibonacci:
    if i%2:
        continue
    print(i)

## with filter
for i in filter(lambda i: not i%2, fibonacci):
    print(i)

## with generator
for i in (j for j in fibonacci if not j%2):
    print(i)

## Numerical and logical functions

## Several built-in functions for working with iterators
## Logical functions any(), all()
## Numerical functions min(), max(), sum()

none_true = [0, 0, 0]
some_true = [0, 1, 0]
all_true = [1, 1, 1]

def check_any(i):
    for e in i:
        if e:
            return True
        return False

check_any(none_true)

## Best way
any(none_true)

## Other way
True in (bool(e) for e in none_true)

def check_all(i):
    for e in i:
        if not e:
            return False
        return True 

## Best way
all(none_true)

False not in (bool(e) for e in none_true)

## Sorted
numbers = [-1, 2, 0, 1]
sorted(numbers)

## Min
sorted(numbers)[-1]
min(numbers)

# Max
sorted(numbers)[0]
max(numbers)

## Sum

def get_sum(i):
    total = 0
    for e in i:
        total += e
    return total

get_sum(numbers)
## Best way
sum(numbers)

## Itertools

## The itertools provide several functions:
## fucntions to create or operate on iterators.
## Select and group elements from iterators.
## Implement combinational logic.

import itertools as it

## count()
for i in it.count(start=10, step=1):
    if not i:
        break
    print(i)

## cycle()
s = "iterators rock"
for i, ch in zip(range(20), it.cycle(s)):
    print(i, ch)

## repeat()
s = "iterators rock"
for i, s in zip(range(10), it.repeat(s)):
    print(i, s)

## chain()
for e in it.chain('abc', [3, 2, 1], 'cba'):
    print(e)

## compress()
sentence = 'iterators', "don't", 'rock'
selector = True, False, True 
for word in it.compress(sentence, selector):
    print(word)

## takewhile()

for i in it.takewhile(lambda x: x < 10, it.count()):
    print(i)

## dropwhile

for i in it.dropwhile(lambda x: x < 5, it.count()):
    if i > 10:
        break
    print()

## groupby

is_even = lambda x: not x%2

for e, g in it.groupby(
        sorted(range(10), key=is_even),
        key=is_even
    ):
    print(e, list(g))

## Combinatorial functions

### product()
for x, y in it.product([0,1,2], [3,4,5]):
    print(x, y)

### permutations()
for i in it.permutations([1,2,3]):
    print(list(i))

### combinations()

for i in it.combinations([1,2,3], r=2)
    print(list(i))
## Functools

