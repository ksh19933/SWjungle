import sys
input = sys.stdin.readline
inf = sys.maxsize
num_house = int(input().strip())
cost = [list(map(int, input().split())) for _ in range(num_house)]

ans = inf
for j in range(3):
    dp = [[0]*3 for _ in range(num_house)]
    dp[0] = [inf] * 3
    dp[0][j] = cost[0][j]
    for i in range(1, num_house):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
    for i in range(3):
        if i != j:
            ans = min(ans, dp[-1][i])
print(ans)


