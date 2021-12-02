import sys
input = sys.stdin.readline
n, m , h = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (h+1) for _ in range(n)]
for b in blocks[0]:
    dp[0][b] = 1
dp[0][0] = 1
for i in range(1, n):
    for b in blocks[i]:
        for j in range(h, b-1, -1):
            dp[i][j] += dp[i-1][j-b]
    for k in range(h+1):
        dp[i][k] = (dp[i][k] + dp[i-1][k])%10007
print(dp[-1][h])
