
# Generators

## A generator is a function with a yield statement.
## Generator are also functions but return output with yield statement.
## They can yield multiple times.
## Receive input with each yield.

## A generator is a type of iterator

def my_generator():

    yield 'a'
    yield 'b'
    yield 'c'

for e in my_generator():
    print(e)

print('d' in my_generator())
False

g = my_generator()
print(g.next())
print(g.next())


## Sending information to a generator

import random

SENTENCES = [
    'How are you?',
    'Fine, thank you',
    'Nothing much',
    'ust chillin'
]

def random_conversation():

    recv = yield 'Hi'
    while recv != 'Bye':
        recv = yield random.choice(SENTENCES)


g = random_conversation()

print(g.send(None))
while True:
    try:
        reply = g.send(input())
    except StopIteration:
        break
    print('>>> ' + reply)
print('Conversation over!')

# Lazy evaluations

## Evaluating what we need only when we need it
## Eager evaluation consumes memory, it is inefficient
## Lazy evaluation is very common in functional programming

def eager_fibonacci(n):

    l = [1,1]
    for i in range(n-2):
        l.append(sum(l[-2:]))
    return l

print(eager_fibonacci(18)

def lazy_fibonacci():

    yield 1
    yield 1
    l = [1, 1]
    while True:
        l = [l[-1], sum(l[-2:])]
        yield l[-1]

for i, f in enumerate(lazy_fibonacci()):
    if i == 10:
        break
    print(f)

# Coroutines - Implementing concurrency through generators

## Rapid alternation ~ parallel
## Generator functions can suspend and resume
## Threfore, multiple generators can run in rapid alternation
## Such generators are often called coroutines

## Multiprocessing = Multiple separate processes
## Each process has its own memory
## Communication between processes is difficult
## The OS decides which process wuns when.

## Threading = Multiple threads within a single process
## Threads share memory
## Communication between threads is easier.
##The operating systems decides chich thread runs when.
## In python, the global interpreter lock makes threading inneficient.

## Couroutines == Functions run in rapid alternation
## More stable and transparent
## The programmer determine which couroutine runs when
## Efficient.
## Cooperative desing

## Example 1

def fibonacci():

    yield 1
    yield 1
    l = [1, 1]
    while True:
        l = [l[-1], sum(l[-2:])]
        yield l[-1]

def tribonacci():
    
    yield 0
    yield 1
    yield 1
    l = [0, 1, 1]
    while True:
        l = [l[-2], l[-1], sum(l[-3:])]
        yield l[-1]

for i, (f, t) in enumerate(zip(fibonacci(), tribonacci())):
    if i == 10:
        break
    print(f, t)


## Example 2

def speaker():

    while True:
        yield random.choice(SENTENCES)

def replier():

    while True:
        recv = yield
        print('Received %s' % recv)
        if recv == 'Bye!':
            break
        print('Replied: %s' % random.choice(SENTENCES))

s = speaker()
r = replier()

r.send(None)
while True:
    recv = s.send(None)
    try:
        r.send(recv)
    except StopIteration:
        break

## Convenience iterators - collections module

## Fields in a regular tuple have an index but no name
## Fields in a named tuple have an index and a name
## Can make code more readable

## A regular dict has no predictable order
## An order dict does have an order.

## Retireven a non-existing key from a regular dict gives a KeyError
## A default dict gives a default value.

## The collections module offers more than this.

## namedtuple

from colections import namedtuple

Person = namedtuple('Person', ['name', 'age'])
Jay_Z = Person(name='Sean Carter', age=47)

name, age = Jay_Z
print("%s is %s years old" % (Jay_Z.name, Jay_Z.age)) # Code more explicit

from collections import OrderedDict

d = OrderedDict([
    ('Lizard','Reptile'),
    ('Whale','Mammal')
])

for species, class_ in d.items():
    print('%s is a %s' % (species, class_))

from collections import defaultdict

favorite_programming_language = {
    'Claire' : 'Assembler',
    'John' : 'Ruby',
    'Sarah' : 'Javascript'
}

d = defaultdict(lambda: 'Python')
d.update(favorite_programming_language)

print(d['Harry'])
# Python
print(d['John'])
# Ruby

## Summary

# 1 Iterators are objects that contain other objects.
# 2 Built-in iterators such as dict, list, tuples and sets.
# 3 Collections module offers other convenient iterators.
# 4 Generators are functions that yield and they are also iterators.
# 5 Generators allow for lazy evaluation and coroutines, or lightweight threading.
