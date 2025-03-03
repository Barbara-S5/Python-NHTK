year = int(input("Введите год ")) 
#if (year <= 2999 and year >= 1000):
year /= 100 
print("Номер столетия: ", int(year + 1))  
