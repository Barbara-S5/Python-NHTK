agh = int(input())
if(9 < agh < 100 or -100 < agh < -9):
  dellen = agh / 10
  fir_var = int(dellen)
  sec_var = agh % 10
  sum = fir_var + sec_var
  if((sum % 2) == 0):
    agh += 2
  else:
    agh -= 2
  print(agh)
else:
  print("Error input")