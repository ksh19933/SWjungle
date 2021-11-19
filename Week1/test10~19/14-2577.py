A = int(input())
B = int(input())
C = int(input())
total = str(A*B*C)
for i in range(10):
  num = 0
  for n in total:
    if(int(n)==i):
      num += 1
  print(num)






