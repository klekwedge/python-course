import random
# from random import randint
# from random import shuffle

x = random.randint(1, 10)
print(x)

my_list = [1, 2, 3]
random.shuffle(my_list)
print(my_list)

from random import shuffle as shuffle_my_list
another_list = [1, 2, 3]
shuffle_my_list(another_list)
print(another_list)
