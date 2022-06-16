# List Comprehension
greeting = 'Hello'
letter_list = []

for letter in greeting:
    letter_list.append(letter)
print(letter_list)

another_letter_list = [letter for letter in greeting]
print(another_letter_list)

str_list = [string for string in '012345678']
print(str_list)

number_list = [num for num in range(10)]
print(number_list)

another_number_list = [num**2 for num in range(10)]
print(another_number_list)

number_list_2 = [-((num - 3)/2)**2 for num in range(10)]
print(number_list_2)


number_list_3 = [6, 43, -2, 11, 4, -532, -12, 431, -4]
new_list = [number**3/2 for number in number_list_3 if number > 0]
print(new_list)

another_new_list = ['+' if number > 0 else '-' for number in number_list_3]
print(another_new_list)
