import sys
n = int(sys.stdin.readline())

sugar = [3, 5]

dp = [10000] * (n+1)
dp[0] = 0

for s in sugar:
    for i in range(s, n+1):
        dp[i] = min(dp[i], dp[i-s] + 1)

if dp[n] == 10000:
    print(-1)
else:
    print(dp[n])