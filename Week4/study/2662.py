# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# arr = [[0] * (m+1)] + [list(map(int, input().split())) for _ in range(n)]
# dp = [[0] *(m+1) for _ in range(n+1)]
# com_dp = [[[0] * (m+1) for _ in range(m+1)] for _ in range(n+1)]
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         dp[i][j] = max(dp[i][j-1], arr[i][j])
#         if dp[i][j] == arr[i][j]:
#             com_dp[i][j][j] = i
#         else:
#             com_dp[i][j] = com_dp[i][j-1].copy()
#         for k in range(1, i+1):
#             # if com_dp[i-arr[0]][j] == 0 :
#             if dp[i][j] < dp[k][j-1] + arr[i-k][j]:
#                 dp[i][j] = dp[k][j-1] + arr[i-k][j]
#                 com_dp[i][j] = com_dp[k][j-1].copy()
#                 com_dp[i][j][j] = i-k
#         # print(dp)
#     # print(com_dp)

# print(dp[-1][-1])
# print(*com_dp[-1][-1][1:])

import sys
from copy import deepcopy
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[0] * (m+1)] + [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)
path = [[] for _ in range(n+1)]
print(arr)
for i in range(n+1):
    dp[i] = arr[i][1]
    path[i].append(i)
print(dp)
print(path)

# for i in range(1, m):
#     for j in range(n, -1, -1):
#         add = 0
#         for i in range(1, j+1):
#             if dp[i] < dp[i-a[0]] + a[j+1]:
#                 dp[i] = dp[i-a[0]] + a[j+1]
                    
# print(dp[-1])
# print(*com_dp[-1])