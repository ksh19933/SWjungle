# import sys
# from math import log2
# sys.setrecursionlimit(1000000)
# def load_box(l1, l2, l3):
#   global cube
#   if l1 == 0 or l2 == 0 or l3 == 0:
#     return 0

#   t = cube[-1][0]
#   while(t >= 0):
#     if not (cube[t][1]):
#       t -= 1
#       continue
#     cube[t][1] -= 1
#     print(f'cube[{t}][1]: {cube[t][1]}')
#     cube_length = pow(2, t)
#     return load_box(l1, l2 - cube_length, l3) + load_box(l1-cube_length, cube_length, l3) + load_box(cube_length, cube_length, l3-cube_length) + 1
#   flag = 0
#   return -1

# l, w, h = map(int, sys.stdin.readline().split())
# cube_num = int(sys.stdin.readline())
# cube = []
# for _ in range(cube_num):
#   cube.append(list(map(int, sys.stdin.readline().split())))
# flag = 1

# if flag == 0:
#   print(-1)
# else:
#   print(load_box(l, w, h))


import sys
from math import log2

l, w, h = map(int, sys.stdin.readline().split())
cube_num = int(sys.stdin.readline())
cube = []
for _ in range(cube_num):
  cube.append(list(map(int, sys.stdin.readline().split())))
cube.reverse()
volume = l * w * h
ans = 0
before = 0
for p, ctn in cube:
  before *= 8
  c_w = 2**p
  maxctn = (l // c_w) * (w // c_w) * (h // c_w) - before
  maxctn = min(ctn, maxctn)
  ans += maxctn
  before += maxctn

if before == volume:
  print(ans)
else:
  print(-1)
