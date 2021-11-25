import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
  i, j, c = map(int, input().split())
  graph[i].append([c, j])
  graph[j].append([c, i])
for i in range(1, n+1):
  graph[i].sort(reverse=True)
start, destination = map(int, input().split())
dis = [0] * (n + 1)
que = []
heappush(que, [0, start])
while que:
  c, v = heappop(que)
  c = -c
  if v == destination:
    print(c)
    break
  if dis[v] > c:
    continue
  for nc, nv in graph[v]:
    if c == 0:
      dis[nv] = nc
      heappush(que, [-dis[nv], nv])
    elif dis[nv] < nc and dis[nv] < c:
      dis[nv] = min(c, nc)
      heappush(que, [-dis[nv], nv])