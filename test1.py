import sys
from heapq import heappush, heappop
from bisect import bisect_left
input = sys.stdin.readline
n, k = map(int, input().split())
ju = []
for i in range(n):
    m , v = map(int, input().split())
    heappush(ju, [-v, m])
bag = []
for i in range(k):
 bag.append(int(input()))
bag.sort()
result = 0
while ju:
    value, mass = heappop(ju)
    value = -value
    idx = bisect_left(bag, mass)
    if idx < len(bag):
        result += value
        bag.pop(idx)
print(result)