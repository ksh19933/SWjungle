import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n, k = map(int, input().split())
ju = []
tmp = []
for i in range(n):
    m , v = map(int, input().split())
    ju.append([m, v])
bag = [int(input()) for _ in range(k)]
ju.sort()
bag.sort()
result = i = 0
for b in bag:
    ## 현재 가방의 무게보다 무게가 작은 보석들을 찾음
    while i < n and ju[i][0] <= b:
        heappush(tmp, -ju[i][1])
        i += 1
    ## 가치가 제일 큰 보석을 tmp에서 빼고 result에 넣는다
    if tmp:
        result -= heappop(tmp)
print(result)