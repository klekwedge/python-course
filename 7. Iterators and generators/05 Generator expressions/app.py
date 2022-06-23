import time


def get_number_from_range():
    for number in range(10):
        yield number


counter = get_number_from_range()

print(counter)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

counter_1 = (number for number in range(10))
print(counter_1)
print(next(counter_1))
print(next(counter_1))
print(next(counter_1))
print(next(counter_1))
print(next(counter_1))
print(next(counter_1))
print(next(counter_1))
print(next(counter_1))
print(next(counter_1))
print(next(counter_1))

print([number for number in range(10)])

################################################################

print(sum([number for number in range(10)]))
print(sum(number for number in range(10)))

import time
list_start_time = time.time()
print(sum([number for number in range(1000000)]))
list_processing_time = time.time() - list_start_time
print(list_processing_time)

gen_start_time = time.time()
print(sum(number for number in range(1000000)))
gen_processing_time = time.time() - gen_start_time
print(gen_processing_time)
