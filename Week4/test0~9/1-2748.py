import sys
input = sys.stdin.readline
n = int(input())
dp = [False] * (n+1)
i = 2
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    dp[0] = 0
    dp[1] = 1
    while i <= n:
        dp[i] = dp[i-1]+dp[i-2]
        i += 1
    print(dp[n])