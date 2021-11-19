import itertools
import sys

num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
target_list = list(map(''.join, itertools.permutations(num, 3)))
n = int(sys.stdin.readline())
print(target_list)
for _ in range(n):
  try_num, target_strike, target_ball = sys.stdin.readline().split()
  remove = 0
  for j in range(len(target_list)):
    strike = 0
    ball = 0
    j -= remove
    for i in range(3):
    #스트라이크 체크
      if target_list[j][i] == try_num[i]:
        strike += 1
    #볼 체크
      elif try_num[i] in target_list[j]:
        ball += 1

    if (strike != int(target_strike)) or (ball != int(target_ball)):
      target_list.remove(target_list[j])
      remove += 1

print(len(target_list))
