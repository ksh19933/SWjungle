import sys
sys.setrecursionlimit(1000000)
def dfs(n):
  visited[n] = True
  for i in gragh[n]:
    if not visited[i]:
      dfs(i)

n, m  = map(int, sys.stdin.readline().split())
gragh = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
  i, j = map(int, sys.stdin.readline().split())
  gragh[i].append(j)
  gragh[j].append(i)

count = 0
for i in range(1, n+1):
  if not visited[i]:
    count += 1
    dfs(i)

print(count)
