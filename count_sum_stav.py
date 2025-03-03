# Вычисление суммы через год под процентную ставку  

p = float(input("Введите процентную ставку "))
x = int(input("Введите сумму рублей вклада "))
y = int(input("Введите сумму копеек вклада "))

sum = x * 100 + y
sum_with_percent = sum * (1 + p / 100)
rub = int(sum_with_percent // 100)
kop = int(sum_with_percent % 100)
print(f"Total {rub} rub, {kop} kop")