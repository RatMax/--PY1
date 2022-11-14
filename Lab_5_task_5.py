from random import sample


def get_random_password(n=8) -> str:
    list1 = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    password = "".join(sample(list1, n))
    return password


print(get_random_password())
