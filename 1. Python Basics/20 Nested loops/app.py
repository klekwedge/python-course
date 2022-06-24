symol = 'o'
counter = 1

while counter < 10:
    list_smiles = []
    for _ in range(counter):
        list_smiles.append(symol)
    str_smiles = ''.join(list_smiles)
    print(str_smiles)
    counter += 1


for number in range(10):
    count = 0
    emoticons = ''
    while count <= number:
        emoticons += 'a'
        count += 1
    print(emoticons)


for number in range(10):
    emoticons = ''
    for count in range(number + 1):
        emoticons += 'e'
    print(emoticons)

# for number in range(11):
#     emoticons = ''
#     for count in range(number):
#         emoticons += 'e'
#     print(emoticons)

for number in range(1, 11):
    print('u' * number)

counter = 1
while counter < 11:
    print('u' * counter)
    counter += 1
