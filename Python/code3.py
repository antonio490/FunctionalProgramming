
# Common funtional design patterns
# A standard solution to a common problem

## Currying - one argument per function
## Reduce a function with multiple arguments
## to a chain of high-order functions that take one argument

def add (a, b, c):

    return a + b + c

print(add(10, 100, 1000))

##

from functools import partial

add_10 = partial(dd, 10)
add_10_100 = partial(add_10, 100)
print(add_10_100(1000))

# Using a decorator it is more pythonic

from inspect import signature

def curry(fnc):

    def inner(arg):

        if len(signature(fnc.parameters) == 1)
            return fnc(arg)
        return curry(partial(fnc, arg))

    return inner

@curry
def add (a, b, c):

    return a + b + c

print(add(10)(100)(1000))

# Monads
# Variables that decide how they should be treat

## A nan is a special numeric value. Any operation on nan
## returns nan. nan * 1 = nan
## nan overrides operations

## The maybe monad is like nan. Any function applied 
## to nothing and returns nothing.

## The list monad defines a series of values. Any function
## applied to a list monads is applied to each element.
## The result is a new ist monad.

def camelcase(s):

    return ''.join((w.capitalize() for w in s.split('_')))

print(camelcase("some_function"))


# Memoization
# Caching to improve performance
# Remembering results

## Once a return value has been determined, a function never needs
# to be called again. That's memoization! 

def prime(n):

    for i in range(n, 0, -1):
        if all([i // x != 1 / x for x in range(i-1, 1, -1)])
            return i

# It takes a long time and we call it again it would take just as long.
print(prime(10000000))

cache = {}

def cached_prime(n):

    if n in cache:
        return cache[n]
    for i in range(n, 0, -1):
        if all([i // x != 1 / x for x in range(i-1, 1, -1)])
            cache[n] = i
            return i      

## Not very elegant -> it works only on these function

def memoize(fnc):

    cache = {}

    def inner(*args):

        if args in cache:
            return cache[args]
        cache[args] = fnc(*args)
        return cache[args]

    return inner

@memoize
def memoized_prime(n):

    for i in range(n, 0, -1):
        if all([i // x != 1 / x for x in range(i-1, 1, -1)])
            return i

print(memoized_prime(100000))
print(memoized_prime(100000))