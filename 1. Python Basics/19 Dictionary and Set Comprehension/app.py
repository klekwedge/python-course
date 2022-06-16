# Dictionary comprehension

number_dict = {'first': 1, 'second': 2, 'third': 3}
new_dict = {key: value**3 for key, value in number_dict.items()}
print(new_dict)

number_list = [6, 43, -2, 11, 4, -532, -12, 431, -4]
another_number_dict = {number: number**2 for number in number_list}
print(another_number_dict)


number_list = [6, 43, -2, 11, 4, -532, -12, 431, -4, 0]
another_number_dict = {number: 'positive' if number >
                       0 else 'negative' if number < 0 else 'zero' for number in number_list}
print(another_number_dict)


# Set comprehension
number_list = [6, 43, -2, 11, 4, -532, -12, 431, -4]
number_set = {number**2 for number in number_list}
print(number_set)

number_set = {number**2 for number in range(3, 11)}
print(number_set)

letter_set  = {letter.upper() for letter in 'hello'}
print(letter_set)