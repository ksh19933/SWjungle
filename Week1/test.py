from itertools import combinations
import sys

n = 1
while n != 0:
  data = list(map(int,sys.stdin.readline().split()))
  n = data.pop(0)


  combi_list = list(combinations(data, 6))
  for i in range(len(combi_list)):
    for j in range(len(combi_list[i])):
      print(combi_list[i][j], end='')
    print()
  print()
