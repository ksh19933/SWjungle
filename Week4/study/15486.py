import sys
input = sys.stdin.readline
n  = int(input())
schedule = [[0,0]] + [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+2)
max_dp = 0
for i in range(1, n+1):
    max_dp = max(max_dp, dp[i])
    if i + schedule[i][0] <= n+1:
        dp[schedule[i][0]+i] = max(max_dp + schedule[i][1], dp[schedule[i][0]+i])
print(max(dp))