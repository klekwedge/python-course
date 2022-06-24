x = 3

if x > 3:
    print('x > 3')
elif x < 3:
    print('x < 3')
else:
    print('x == 3')


day_time = 'afternoon'

if day_time == 'morning':
    print('Monster wakes up')
elif day_time == 'afternoon':
    print('Monster is walking')
elif day_time == 'evening':
    print('Monster is eating')
elif day_time == 'night':
    print('Monster is sleeping')
else:
    print('Monster do something')


y = 45

if y % 2 == 0:
    print('y is even')
else:
    print('y is odd')
print('Sometext')


user_input = input('Input something')

if user_input == 'Hello':
    print('Hello, nice to meet you')


if 1:
    print('Something')

# if 0:
#   print('Something')

if 'c':
    print('Something')

# if '':
#   print('Something')

# if None:
#   print('Something')

if [1, 3]:
    print('Something')

# if []:
#   print('Something')

# False: 0, empty string, None, empty object

lucky_number = input('Enter a number')
if lucky_number:
    print(lucky_number + ' is your lucky number!')
else:
    print('You have to enter some number')
