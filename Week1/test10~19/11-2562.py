maximum = 0
max_lo = 0
for i in range(9):
  num = int(input())
  if num > maximum:
    maximum = num
    max_lo = i+1
print(maximum)
print(max_lo)