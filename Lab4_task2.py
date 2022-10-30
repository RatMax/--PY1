def get_count_char(str_):
    str_lower = str_.lower()
    str_split = str_lower.split()
    str_join = ''.join(str_split)
    str_new = ''
    for i in range(len(str_join)-1):
        if str_join[i].isalpha() == 1:
            str_r = str_ew + str_join[i]
    count_dict = {str_r[i]: str_r.count(str_r[i]) for i in range(len(str_new)-1)}
    return count_dict
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
