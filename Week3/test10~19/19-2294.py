# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())

# coins = [int(input()) for _ in range(n)]

# dp = [10001] * (k+1)
# dp[0] = 0
# coins.sort()
# for coin in coins:
#   for i in range(coin, k+1):
#     dp[i] = min(dp[i], dp[i-coin] + 1)
# if dp[k] == 10001:
#   print(-1)
# else:
#   print(dp[k])


import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
coins = set(int(input()) for _ in range(n))
check = [0] * (k+1)
que = deque()

for coin in coins:
  if coin <= k:
    que.append([coin, 1])
    check[coin] = 1
flag = 0
while que:
  val, cnt = que.popleft()
  if val == k:
    flag = 1
    print(cnt)
    break
  for coin in coins:
    if val + coin > k:
      continue
    elif check[coin+val] == 0:
      check[coin+val] = 1
      que.append([coin+val, cnt+1])

if flag == 0:
  print(-1)