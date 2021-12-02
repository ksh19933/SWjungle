import sys
input = sys.stdin.readline
inf = sys.maxsize
case_num =  int(input())

for _ in range(case_num):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[0] * n for _ in range(n)]
    for d in range(1, n):
        for i in range(n-d):
            j = i + d
            dp[i][j] = inf
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
            dp[i][j] += sum(arr[i:j+1])
    print(dp[0][-1])
