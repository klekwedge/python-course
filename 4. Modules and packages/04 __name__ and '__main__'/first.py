# print(1)
# print('string')

# # __name__ = '__main__'
# print(__name__)


# def function1():
#     pass


# def function2():
#     pass


# if __name__ == '__main__':
#     function1()
#     function2()


def function_1():
    print('function_1() from first.py')


print('Top level in first.py')

if __name__ == '__main__':
    print('first.py is being run directly')
else:
    print('first.py has been imported')
