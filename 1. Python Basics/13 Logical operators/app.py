x = 1
y = 2

print(x > 1)
print(y > 1)


# and, or, not
print(x > 1 and y > 1)
print(x > 1 or y > 1)
print(not x > 1 and y > 1)

print(True and True)
print(True or True)
print(not True)

print(False and False)
print(False or False)
print(not False)

print(True and False)
print(True or False)


name = 'John'
age = 21
is_married = False

if age > 18 and is_married == False:
  print('Hello {}! You can find a girl here'.format(name))