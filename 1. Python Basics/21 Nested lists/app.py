nested_list = [[1, 2, 3, 784, 2112, 6583], [4, 5, 6], [7, 8, 9, 849]]
print(nested_list)

print(len(nested_list))
print(len(nested_list[0]))
print(len(nested_list[-1]))

print(nested_list[1][1])
print(nested_list[-1][-2])
print(nested_list[-1][2])

for inner_list in nested_list:
    for number in inner_list:
        print(number)

[[print(number) for number in inner_list] for inner_list in nested_list]
