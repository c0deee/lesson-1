from random import randint

count_numbers = int(input('сколько чисел'))
number_to_find = int(input('искомое число'))
numbers = [randint(0, 9) for _ in range(count_numbers)]

print('числа -- ', numbers)
print(f'искомое число {number_to_find} встречается {numbers.count(number_to_find)} раз')
