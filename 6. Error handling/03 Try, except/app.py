from typing import Type


print('Some code')
# print(my_variable)

try:
    print(len(23))
    print(my_variable)
except NameError:
    print('NameError has happen')
except TypeError:
    print('TypeError has happen')

print('Code after error')

user_dict = {'first_name': 'Jack', 'last_name': 'white', 'age': 24}
print(user_dict['first_name'])
# print(user_dict['name'])

print(user_dict.get('first_name'))
print(user_dict.get('name'))


def get_dict_values(dict, key):
  '''
  if dict has not 
  '''
  try:
    return dict[key]
  except KeyError:
    return None

print(get_dict_values(user_dict, 'age'))
print(get_dict_values(user_dict, 'a'))
print(get_dict_values(user_dict, 'first_name'))