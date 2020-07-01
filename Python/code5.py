
# Dictionaries - Mutable, Key-Value mapping without a fixed order.

## A dict is a collection of key-value mappings.
## Elements dont have a position, instead we use keys to index them.
## Keys can be any python object.

d = {'Praying Manties' : 'Insect', 'Whale' : 'Mammal'}

print(d)

## Add new element
d['Lizard'] = 'Reptile'

## Iteration
for species in d:
    print(species)

for class_ in d.values():
    print(class_)

for species, class_ in d.items():
    print(species, class_)

while d:
    species, class_ = d.popitem()
    print(species, class_)

# Using a SET - Inmutable collections of unique elements without fixed order.

## Each element occur only once
## SETS are generally use on mathematical concepts.

mammals = {'Human', 'Whale', 'Dog', 'Cat'}

print(mammals)

# Adding and removing
mammals.add('Mouse')
mammals.remove('Dog')

mammals = {'Human', 'Whale', 'Dog', 'Cat'}
pets = {'Dog', 'Cat', 'Goldfish'}

## Union
print(mammals | pets)
{'Human', 'Whale', 'Dog', 'Cat', 'Goldfish'}

## Intersection
print(mammals & pets)
{'Dog', 'Cat'}

## Difference
print(mammals - pets)
{'Whale', 'Human'}

## Subset
print(mammals < pets)
False