import sys
input = sys.stdin.readline
inf = sys.maxsize
n, m = map(int, input().split())
# 건너지 못하는 돌
small_rocks = set()
for i in range(m):
    small_rocks.add(int(input()))

k = int((2*n)**0.5) + 1
dp = [[inf] * (k+1) for _ in range(n+1)]
dp[1][0] = 0

for i in range(2, n+1):
    if i in small_rocks:
        continue
    for j in range(1, k):
        dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1
if min(dp[n]) == inf:
    print(-1)
else:
    print(min(dp[n]))