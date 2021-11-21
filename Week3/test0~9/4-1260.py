import sys
from collections import deque

def dfs(n):
  print(n, end=' ')
  visited[n] = True
  for i in gragh[n]:
    if not visited[i]:
      dfs(i)

def bfs(n):
  visited[n] = True
  que = deque([n])
  while que:
    v = que.popleft()
    print(v, end=' ')
    for i in gragh[v]:
      if not visited[i]:
        visited[i] = True
        que.append(i)

n, m, v = map(int, sys.stdin.readline().split())
visited = [False] * (n+1)
gragh = [[] for _ in range(n+1)]

for _ in range(m):
  i, j = map(int, sys.stdin.readline().split())
  gragh[i].append(j)
  gragh[j].append(i)

for i in range(1, n+1):
  gragh[i].sort()

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)