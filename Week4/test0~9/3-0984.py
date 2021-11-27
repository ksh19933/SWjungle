import sys
input = sys.stdin.readline
case_num = int(input())
for _ in range(case_num):
    coin_num = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    dp = [0] * (target+1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, target+1):
            dp[i] += dp[i-coin]
    print(dp[target])