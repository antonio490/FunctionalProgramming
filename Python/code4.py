# Exceptions

## An exception is an object just like everythin in Python
## Can be part of a raise statement.
## This causes the program to crash.
## Both raising and catching exceptions are statements, but
## statements are not allow on lambda functions.

def add_str(s):

    try:
        return sum([int(i) for i in s.split("+")])
    except AttributeError:
        return None

print(add_str(1+2))

## With lambda

l_add_str = lambda s: sum([int(i) for i in s.split("+")])

print(l_add_str(1+2))

# Handling errors with lambda functions

l_add_str = lambda s: sum([int(i) for i in s.split("+")])

## Maybe-like decorator

def maybe(fnc):

    def inner(*args):

        for a in args:
            if isinstance(a, Exception):
                return a
        try:
            return fnc(*args)
        except Exception as e:
            return e

    return inner

safe_add_str = maybe(lambda s: sum([int(i) for i in s.split("+")]))

print(safe_add_str(1+2))