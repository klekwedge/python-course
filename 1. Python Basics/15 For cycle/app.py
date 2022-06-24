number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in number_list:
    print(number)
    print('Hello')

for number in number_list:
    if number % 2 == 0:
        print(number)
    else:
        print('Hey')


list_numbers_sum = 0
for number in number_list:
    list_numbers_sum += number
print(list_numbers_sum)


greeting = 'Hello Python'
for letter in greeting:
    print(letter)

for letter in greeting:
    if letter == 'o':
        print(letter)

for letter in greeting:
    if letter != 'o':
        print(letter)


for letter in 'Hello Python':
    if letter != 'o':
        print(letter)


for letter in 'Hello Python':
    print('One more letter!')


tuple_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
for item in tuple_list:
    print(item)

for letter_1, letter_2 in tuple_list:
    print(letter_1, letter_2)

another_tuple_list = [('a', 'b', 1), ('c', 'd', 4), ('e', 'f', 5)]
for letter_1, letter_2, number in another_tuple_list:
    print(letter_1, letter_2, number)

dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for item in dictionary:
    print(item)

for item in dictionary.items():
    print(item)

for key, value in dictionary.items():
    print(key)
    print(value)
#######################################
for item in dictionary.keys():
    print(item)

for item in dictionary.values():
    print(item)
#######################################

for x in range(5):
    print(x)
    print('Hello')


for _ in range(5):
    print('Hi')
