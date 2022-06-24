def print_greeting():
    '''
    Print 'Hello!' text
    :return: None
    '''
    print('Hello!')


print_greeting()
help(print_greeting)


def print_greeting_with_name(name='Name'):
    '''
    :param name:
    :return: None
    '''
    print('Hello, ' + name + '!')


print_greeting_with_name('Alex')
help(print_greeting_with_name)
print_greeting_with_name()

x = print_greeting_with_name('Jack')
print(x)


def sum_of_two_numbers(a=0, b=0):
    '''
    :param a: The first addend
    :param b: The second addend
    :return: Sum of a and b
    '''
    return a + b


x = sum_of_two_numbers(5, 1)
print(x)
print(sum_of_two_numbers(1200))
help(sum_of_two_numbers)


def is_hello_in_text(text):
    if 'hello' in text.lower():
        return True
    else:
        return False


print(is_hello_in_text('hello Jack'))


def is_hi_in_text(text):
    return 'hi' in text.lower()


print(is_hi_in_text('hi Jack'))


def is_string_in_text(string, text):
    return string in text


print(is_string_in_text('hello', 'hello Jack'))


def another_greeting(name, gender):
    if gender == 'male':
        print('Hello ' + name + '! You look great!')
        return gender
    elif gender == 'female':
        print('Hello ' + name + '! You look amazing!')
        return gender
    else:
        print('Hello ' + name + '! You look nice!')
        return gender


returned_value_1 = another_greeting('Jack', 'male')
returned_value_2 = another_greeting('Jane', 'female')
returned_value_3 = another_greeting('Ja', 'cmale')

print(returned_value_1)
print(returned_value_2)
print(returned_value_3)
