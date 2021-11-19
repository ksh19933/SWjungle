num1 = int(input())
num2 = int(input())
while num2 != 0:
  print(num1*(num2%10))
  num2 = num2 // 10
print(num1*num2)