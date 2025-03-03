# угол (в градусах), на который повернулась часовая стрелка с начала суток 

h = int(input("Введите часы "))
m = int(input("Введите минуты "))
s = int(input("Введите секунды "))
if (0 <= h < 12 and 0 <= m < 60 and 0 <= s < 60):
  sum = 30 * h + 0.5 * m + (0.5 / 60) * s 
  print(int(float(sum)))
else:
  print("Error input")