from math import pi
pi = 'outer pi variable'


def print_pi():
    pi = 'inner pi variable'
    print(pi)


print_pi()
print(pi)


# Local Scope

pi = 'global pi variable'


def inner():
    pi = 'inner pi variable'
    print(pi)


inner()

# Global Scope

pi = 'global pi variable'


def inner():
    pi = 'inner pi variable'
    print(pi)


inner()
print(pi)

# Enclosed Scope

pi = 'global pi variable'


def outer():
    pi = 'outer pi variable'

    def inner():
        # pi = 'inner pi variable'
        nonlocal pi
        pi = 'new outer pi variable'
        print(pi)
    inner()
    print(pi)


outer()
print(pi)


pi = 'global pi variable'


def outer():
    pi = 'outer pi variable'

    def inner():
        global pi
        pi = 'new value'
        print(pi)
    inner()
    print(pi)


outer()
print(pi)


# Built-in Scope

# pi = 'global pi variable'


def outer():
    # pi = 'outer pi variable'
    def inner():
        # pi = 'inner pi variable'
        print(pi)
    inner()


outer()
