def delete(list_, index=None):
    if index != None:
        s1 = list_[:index]
        s2 = list_[index+1:]
        s = s1 + s2
    else:
        s = list_[:len(list_)-1]
    return s

    ...  # TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
