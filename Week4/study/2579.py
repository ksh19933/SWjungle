import sys
input = sys.stdin.readline
n = int(input())
p = [int(input()) for _ in range(n)]
if n > 2:
    dp = [0] * (n+1)
    dp[0], dp[1], dp[2] = 0, p[0], p[0]+p[1]
    for i in range(3, n+1):
        dp[i] = max(p[i-1]+p[i-2]+dp[i-3], p[i-1]+dp[i-2])
    print(dp[n])
else:
    print(sum(p))