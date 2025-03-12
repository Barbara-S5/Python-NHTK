A = 10
B = 15
N = 0
if (A >= B):
  print("Error")

for num in range(B-1, A, -1):
  print(num, end = " ")
  N += 1
print("\n")
print(f"Amount of numbers:", N)