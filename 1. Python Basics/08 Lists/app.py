number_list = [32, 21, 48, 34.56]
print(number_list)

some_list = [12, 35.3, 'example']
print(some_list)

print(len(some_list))
print(some_list[1])

another_list = some_list[:2]
print(another_list)

some_list[2] = 'Hello!'
print(some_list)

new_list = some_list + another_list
print(new_list)

# Adding items

# new_list[5] = 'New item'
# print(new_list)

# Append
new_list.append('New item')
print(new_list)

# Insert
new_list.insert(0, 'World')
print(new_list)

new_list.insert(3, 123321)
print(new_list)

# Removing items
# Pop
new_list.pop()  # (-1)
print(new_list)

new_list.pop(0)
print(new_list)

new_list.pop(-3)
print(new_list)

print(new_list.pop(-3))
print(f'New list {new_list}')

# Remove
new_list.remove(12)
print(f'New list {new_list}')

deleted = new_list.remove(12)
print(deleted)

# Sort  
number_list = [45, 12, 3212, 3432, 556]
letter_list = ['s', 'w', 'c', 'f']

print(f'Number list {number_list}')
print(f'Letter list {letter_list}')

number_list.sort()
letter_list.sort()

print(f'Number list {number_list}')
print(f'Letter list {letter_list}')

# Reverse  
number_list.reverse()
letter_list.reverse()

print(f'Number list {number_list}')
print(f'Letter list {letter_list}')

number_list.append(letter_list)
print(number_list)