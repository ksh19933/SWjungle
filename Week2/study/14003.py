# import sys
# from collections import deque
# n = int(sys.stdin.readline())
# num_arr = list(map(int, sys.stdin.readline().split()))


# ##dp이용?
# dp = [1] * n
# for i in range(n):
#   for j in range(i):
#     if num_arr[i] > num_arr[j] and dp[i] < dp[j] + 1:
#       dp[i] = dp[j] + 1

# print(dp)
# max_idx = dp.index(max(dp))
# c = dp[max_idx]
# de = deque()
# for i in range(n-1, -1, -1):
#   if c == dp[i] + 1:
#     c = dp[i]
#     de.append(num_arr[i])

# de.appendleft(num_arr[max_idx])

# print(de)

import sys

def lower_bound(pl, pr, key):
  while pl < pr:
    pc = (pl + pr) // 2
    if temp[pc] < key:
      pl = pc + 1
    else:
      pr = pc
  return pl

n = int(sys.stdin.readline())
num_arr = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(n + 1)] 
temp = [-1000000001] 
maxVal = 0

for i in range(1, n+1):
  if temp[-1] < num_arr[i]:
    temp.append(num_arr[i])
    dp[i] = len(temp) - 1
    maxVal = dp[i] # 부분 수열의 최대 길이
  else:
    #작을 경우
    dp[i] = lower_bound(0, len(temp)-1, num_arr[i])
    temp[dp[i]] = num_arr[i]

print(dp)
print(maxVal)
result = []
for i in range(n, 0, -1):
  if maxVal == dp[i]:
    maxVal -= 1
    result.append(num_arr[i])

print(*(result[::-1]))



