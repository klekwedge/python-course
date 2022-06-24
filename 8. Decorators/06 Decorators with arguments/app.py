from functools import wraps


def check_if_first_arg_is(value):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] != value:
                print(f'FIrst argument has to be {value}')
            return func(*args, **kwargs)
        return wrapper
    return inner_dec


@check_if_first_arg_is('red')
def print_rainbow_colors(*colors):
    print(colors)


@check_if_first_arg_is(7)
def multiply_seven(a, b):
    return a * b


print_rainbow_colors('red', 'orange', 'yellow', 'green',
                     'blue', 'indigo', 'violet')

print(multiply_seven(7, 4))


def enforce(*types):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_args = []
            for a, t in zip(args, types):
                new_args.append(t(a))
            return func(*new_args, **kwargs)
        return wrapper
    return inner_dec


@enforce(str, int)
def print_text_n_times(text, n):
    for number in range(n):
        print(text)

print_text_n_times('Hi', 5)
print_text_n_times('Hi', '5')

# *args - ('Hi', '5')
# *types - (str, int)
# zip(args, types) - ('Hi', str) ('5', int)


@enforce(float, float)
def divide(a, b):
    return a / b


print(divide(4, 2))
print(divide('4', '2'))