# import sys
# input = sys.stdin.readline

# n = int(input())

# arr = [list(map(int, input().split())) for _ in range(n)]

# dp = [0] * 3
# for i in range(1, n+1):
#     temp = dp.copy()
#     dp[0] = max(temp[0], temp[1]) + arr[i-1][0]
#     dp[1] = max(temp[0], temp[1], temp[2]) + arr[i-1][1]
#     dp[2] = max(temp[2], temp[1]) + arr[i-1][2]
# print(max(dp), end = " ")
# dp = [0] * 3
# for i in range(1, n+1):
#     temp = dp.copy()
#     dp[0] = min(temp[0], temp[1]) + arr[i-1][0]
#     dp[1] = min(temp[0], temp[1], temp[2]) + arr[i-1][1]
#     dp[2] = min(temp[2], temp[1]) + arr[i-1][2]
# print(min(dp))

import sys
n = int(sys.stdin.readline())
min_num = [0, 0, 0]
max_num = [0, 0, 0]
for _ in range(n):
    n1, n2, n3 = list(map(int, sys.stdin.readline().split()))
    max_num[0], max_num[1], max_num[2] = max(max_num[0], max_num[1]) + n1,\
                                         max(max_num[0], max_num[1], max_num[2]) + n2,\
                                         max(max_num[2], max_num[1]) + n3
    min_num[0], min_num[1], min_num[2] = min(min_num[0], min_num[1])+ n1,\
                                         min(min_num[0], min_num[1], min_num[2]) + n2,\
                                         min(min_num[2], min_num[1]) + n3
print(max(max_num), min(min_num))