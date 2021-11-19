import sys
def tree_cut(pl, pr, K):
  while (pl <= pr):
    pc = (pl + pr)//2
    result = 0
    for height in height_list:
      if pc < height:
        result += (height-pc)
    if K <= result:
      pl = pc + 1
    else: #K > result:
      pr = pc - 1
  print(pr)

N, K = map(int, sys.stdin.readline().split())
height_list = list(map(int, sys.stdin.readline().split()))

height_list.sort()

tree_cut(height_list[0], height_list[-1], K)