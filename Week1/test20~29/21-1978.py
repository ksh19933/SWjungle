import sys
import math
N = int(sys.stdin.readline())
num_arr = list(map(int, sys.stdin.readline().split()))
ctn = 0
for num in num_arr:
  if num > 1:
    prime_check = True
    for i in range(2, int(math.sqrt(num) +1)):
      if num % i == 0:
        prime_check = False
        break
    if prime_check:
      ctn += 1
print(ctn)
