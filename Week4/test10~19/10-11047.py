import sys
input = sys.stdin.readline
coin_num, target_value = map(int, input().split())
coins = [int(input()) for _ in range(coin_num)]
coins.sort(reverse=True)
cnt = 0
for coin in coins:
    cnt += target_value // coin
    target_value = target_value % coin
    if target_value == 0:
        break

print(cnt)
    