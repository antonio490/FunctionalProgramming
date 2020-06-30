# Functions as arguments

## High order functions:  Any function that operates other functions
## A function in python is an object

l_factorial = lambda n: 1 if n==0 else n*l_factorial(n-1)

import time

t0 = time.time()
l_factorial(9000)
t1 = time.time()

print("Took: %.5f s" % (t1-t0))

# -> Functional way

def time(fnc, arg):
    t0 = time.time()
    l_factorial(9000)
    t1 = time.time()
    return t1 -t0

print("Took: %.5f s" % timer(l_factorial, 900))

# -> Now with lambda

l_timestamp = lambda fnc, arg: (time.time(), fnc(arg), time.time())
l_diff = lambda t0, retval, t1: t1-t0
l_timer = lambda fnc, arg: l_diff(*l_timestamp(fnc, arg))

print("Took: %.5f s" % l_timer(l_factorial, 900))

# Nested functions

def outer():
    def inner():

        print("I\'m inner")
    
    inner()
outer()


def outer():
    def inner():

        x ="inner"
        print("inner:\t\t", x)
    
    x = "outer"
    print("Outer (before):\t", x)
    inner()
    print("Outer (fater):\t", x)

x = "global"
print("Global (before):\t", x)
outer()
print("Global (after):\t", x)

# Functions as return values

def perform_steps(*functions):

    for function in functions:
        function()

perform_steps(preheat_oven(), 
                put_croissants(), 
                wait_five_minutes(), 
                take_croissants())


## High order function example

def create_recipe(*functions):

    def run_all():
        for function in functions:
            function()
        return run_all

recipe = create_recipe(preheat_oven(), 
                put_croissants(), 
                wait_five_minutes(), 
                take_croissants_out())
recipe()

# The operator module

l_factorial = lambda n: 1 if n==0 else n*l_factorial(n-1)

def chain_mul(*what):
    """Takes a list of (functions, argument) tuples. Calls each function
    with its argument, multiplies up the return values, (starting at 1) 
    and returns the total."""

    total = 1
    for (fnc, arg) in what:
        total *= fnc(arg)
    return total

chain_mul( (l_factorial, 2), (l_factorial, 3) )

##
import operator

def chain(how, *what):

    total = 1
    for (fnc, arg) in what:
        total = how(total, fnc(arg))
    return total

chain(operator.mul, (l_factorial, 2), (l_factorial, 3)  )
chain(operator.truediv, (l_factorial, 2), (l_factorial, 3)  )

# Decorators
# A way to wrap a function around a function
# Allows you to add functionality to a function

def factorial(n):

    return 1 if n == 0 else n*factorial(n-1)


import time

def timer(fnc):

    def inner(arg):

        t0 = time.time()
        fnc(arg)
        t1 = time.time()
        return t1-t0

    return inner

timed_factorial = timer(factorial) # This is a decorator
timed_factorial(500)

@timer
def timed_factorial(n):

    return 1 if n == 0 else n*factorial(n-1)

timed_factorial(500)

# Decorators with arguments
# A decorator with arguments is a function that returns 
# a decorator. It requires nesting within nesting

def timer_with_arguments(units='s'):

    def timer(fnc):

        def inner(arg):

            t0 = time.time()
            fnc(arg)
            t1 = time.time()
            diff = t1-t0
            if units == 'ms':
                diff *= 1000
            return diff

        return inner
    
    return timer

timed_factorial = timer_with_arguments(units='ms')(factorial)
timed_factorial(500)

@timer_with_arguments(units = 's')
def factorial(n):
        
    return 1 if n == 0 else n*factorial(n-1)

factorial(500)