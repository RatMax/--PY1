from random import randint

def get_unique_list_numbers() -> list[int]:
    i = 1
    num_list = [randint(-10, 10)]
    while i <16:
        num = randint(-10, 10)
        if not num in num_list:
            num_list.insert(i,num)
            i+=1
    return num_list

    ...  # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
