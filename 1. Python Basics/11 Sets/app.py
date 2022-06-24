rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue',
                  'indigo', 'violet'}
print(rainbow_colors)
print(type(rainbow_colors))

# empty_set = {}
# print(empty_set)
# print(type(empty_set))

empty_set = set()
print(empty_set)
print(type(empty_set))

number_list = [1, 43, 56, 3, 5, 3]
text_tuple = ('sfa', 'fdsaa', 'cgcfw', 'sfa', 'sfa')

set_from_list = set(number_list)
set_from_tuple = set(text_tuple)

set_from_list.add(123)
set_from_tuple.add('Hello')

set_from_list.add(123)
set_from_tuple.add('Hello')

x = set_from_list.pop()
y = set_from_list.remove(56)
print(x, y)

set_from_list.discard(5)

# set_from_list.remove(5321) Wrong
set_from_list.discard(4642)  # Right

print(set_from_list)
print(set_from_tuple)

set_from_list.clear()
print(set_from_list)
