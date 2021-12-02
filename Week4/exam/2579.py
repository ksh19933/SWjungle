import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
if n == 1:
    print(arr[0])
else:
    dp = [0] * (n)
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    for i in range(2, n):
        dp[i] = max(arr[i] + dp[i-2], arr[i]+arr[i-1]+dp[i-3])
    print(dp[-1])
