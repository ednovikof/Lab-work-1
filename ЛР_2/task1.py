money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

m = -1   # Количество месяцев (-1 т.к. алгоритм учитывает месяц с долгами)
w = 0   # Расходы

for _ in range(1):
    w = salary - spend
    money_capital += w
    m += 1
    while money_capital >= 0:
        w = salary - (spend * (1+increase))
        spend = spend * (1+increase)
        money_capital += w
        m += 1
print("Количество месяцев, которое можно протянуть без долгов:", m)
