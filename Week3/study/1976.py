import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
visited = [False] * (n+1)

arr = [list(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n+1)]
for i in range(n):
  for j in range(n):
    if arr[i][j] == 1:
      graph[i+1].append(j+1)


target = list(map(int, input().split()))

que = deque([target[0]])
visited[target[0]] = True
while que:
  n = que.popleft()
  for v in graph[n]:
    if not visited[v]:
      que.append(v)
      visited[v] = True


for t in target:
  if not visited[t]:
    print("NO")
    exit(0)
print("YES")
