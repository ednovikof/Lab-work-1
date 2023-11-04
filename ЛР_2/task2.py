salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0   # Исходный капитал
i = 1               # Количество месяцев без %
for _ in range(1):
    w = salary - spend
    money_capital -= w
for _ in range(months - i):
    w = salary - (spend * (1 + increase))
    spend = spend * (1 + increase)
    money_capital -= w

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital, 2))
