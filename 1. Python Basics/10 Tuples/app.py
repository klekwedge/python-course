tuple_1 = 1, 2, 5
tuple_2 = ('One', 'Hello!', 'World')
tuple_3 = (5, 1.2, 'Hi')

print(tuple_1)
print(tuple_2)
print(tuple_3)

print(type(tuple_1))

print(tuple_1[1])
# tuple_1[1] = 3

new_tuple = (tuple_1[0], 3, tuple_1[2])
# new_tuple = (tuple_1[0], 3, tuple_1[-1])

x = y = z = 12
print(x, y, z)

x, y, z = 12, 13, 14
print(x, y, z)

person_tuple = ('John', 'Smith', 1986)
print(person_tuple)

first_name, last_name, year_of_birth = person_tuple
print(first_name, last_name, year_of_birth)

t1 = (1, 2, 5, 1, 7, 9)
print(t1.count(1))
print(t1.count(7))
print(t1.count(71))

greetings_tuple = ('Hello', 'Hi', 'Hi')
print(greetings_tuple.count('Hello'))

print(t1.index(5))
print(greetings_tuple.index('Hello'))