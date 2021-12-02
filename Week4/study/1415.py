import sys
input = sys.stdin.readline

n = int(input())
candy = []
candy_num = [0] * 10001
zero_num = 1

for _ in range(n):
    num = int(input())
    if num == 0:
        zero_num += 1
        continue
    if not candy_num[num]:
        candy.append(num)
    candy_num[num] += 1


prime_check = [True]*(500005)
for i in range(2, 500001):
    if prime_check[i]:
        for k in range(i+i, 500001, i):
            prime_check[k] = False

dp = [0] * 500005
dp[0] = 1
for c in candy:
    for i in range(500000, -1, -1):
        for j in range(1, candy_num[c]+1):
            if (i-c*j <0): break
            dp[i] += dp[i-c*j]

ans = 0
for j in range(2, 500001):
    if prime_check[j]:
        ans += dp[j]

ans *= zero_num
print(ans)

