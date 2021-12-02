import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
if n > 2:
    dp = [0] * 20
    dp[0], dp[1] = arr[0], arr[0] + arr[1]
    dp[2] = max(dp[1], arr[0] + arr[2], arr[1] + arr[2])
    for i in range(3, n):
        dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i], dp[i-1])
        print(dp)
    print(max(dp))
elif n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0]+arr[1])