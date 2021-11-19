# import math
import sys
def moduler(a, b):
  if b == 1:
    return a % c
  temp = moduler(a, b//2)
  if b%2 == 0:
    return temp * temp % c
  else:
    return temp * temp * a % c
  # return  (moduler(a, b//2) * moduler(a, math.ceil(b/2))) % c
a, b, c = map(int, sys.stdin.readline().split())
print(moduler(a, b))
