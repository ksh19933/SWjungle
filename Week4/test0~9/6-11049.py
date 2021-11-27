import sys
input = sys.stdin.readline

arr_num = int(input())
max = 2**32
arr = [list(map(int, input().split())) for _ in range(arr_num)]
print(arr)
dp = [[0] * arr_num for _ in range(arr_num)]

for d in range(arr_num):
    for i in range(arr_num - d):
        j = i + d
        if i == j:
            continue
        dp[i][j] = max
        for k in range(i,j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + arr[i][0]*arr[k][1]*arr[j][1])

print(dp[0][-1])