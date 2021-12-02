import sys
n = int(sys.stdin.readline())
dp = [1, 1]
if n == 1:
    print(1)
else:
    for i in range(2, n+1):
        dp[1], dp[0] = (dp[1] + dp[0])%10007, dp[1] 
    print(dp[1])
