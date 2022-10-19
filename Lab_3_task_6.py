list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
for i in list_numbers:
    if i == max( list_numbers):
       num = list_numbers.index(i)

list_numbers[num], list_numbers[-1] = list_numbers[-1], list_numbers[num]

print(list_numbers)
