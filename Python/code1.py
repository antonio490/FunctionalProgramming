
# Lambda functions
# A fomal mathematical system to express functions
# Expressions not statements

def p_pythogoras(x, y):
    return sqrt(x**2 + y**2)

p_pythogoras(1,1)

##

l_pythogoras = lambda x, y: sqrt(x**2 + y**2)
l_pythogoras(1,1)

##

def f_factorial(n):
    return 1 if n==0 else n*f_factorial(n-1)

f_factorial(3)

##

l_factorial = lambda n: 1 if n==0 else n*l_factorial(n-1)
l_factorial(3)

## When lambda's are convenient

# map(function, iter)

l = [0,1,2,3,4]
list(map(lambda x: x*2, l))

# List comprehension
print([x * 2 for x in range(2)])

## Use 'and' and 'or' as flow control.

# AND -> Gives the first element is not True.
# OR -> Gives us the last value if all values are False.

def my_and(*values):

    for value in values:
        if not value:
            return value
    return value

def my_or(*values):
    for value in values:
        if value:
            return value
    return value

ANIMALS = 'mammal', 'reptile', 'anphibian', 'bird'
EGG_LAYING_ANIMALS = 'reptile', 'anphibian', 'bird'

is_animal = lambda animal: animal in ANIMALS
animal_lays_eggs = lambda animal: print('x') or animal in EGG_LAYING_ANIMALS

lays_eggs = lambda thing: is_animal(thing) and animal_lays_eggs(thing)
lays_eggs('reptile')

## if statements should be used in functional programming but if expressions can.

def p_grade_description(gp):

    if gp > 7:
        return 'good'
    if gp > 5:
        return 'sufficient'
    return 'insufficient'

p_grade_description(8)

## Same function above with lambda function

(lambda gp: 'good' if gp > 7 else 'sufficient' if gp > 5 else 'insufficient')(8)
