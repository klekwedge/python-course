# range
from random import randint
from random import shuffle
for x in range(10):
    print(x)

for x in range(3, 10):
    print(x)

for x in range(3, 10, 3):
    print(x)

print(range(10))
print(type(range(10)))

print(list(range(10)))

# enumerate
letter_index = 0
my_string = 'afgctieokv'
for letter in my_string:
    print(letter + ' is at index ' + str(letter_index))
    letter_index += 1

for item in enumerate(my_string):
    print(item)

for index, letter in enumerate(my_string):
    print(letter + ' is at index ' + str(index))

# in
print('a' in 'Jack')
print('b' in 'Jack')
print(str(1) in 'Jack')

letter_list = ['a', 'b', 'c']

print('a' in letter_list)
print(1 in letter_list)
print(True in letter_list)

dict_1 = {1: 'a', 2: 'b', 3: 'c'}

print(1 in dict_1)
print('a' in dict_1)

print(1 in dict_1.keys())
print('a' in dict_1.values())

# min / max
print(min(1, 3, 4, 56, 64, 1, 21))
print(max(1, 3, 4, 56, 64, 1, 21))

my_list = [1, 4532, 632, 25, 331]
print(max(my_list))

print(max('Hello'))

for letter in 'Hello':
    print(ord(letter))

# random
my_list = [1, 4532, 632, 25, 331, 231, 665, 31]
shuffle(my_list)
print(my_list)

print(randint(1, 10))
print(randint(12, 100))
