salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
i = 1
need_money = 0  # количество денег, чтобы прожить 10 месяцев

while i <= months:
    need_money = spend * ( 1 + increase ) ** (i-1) - salary + need_money
    i += 1
print(round(need_money))
