import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

indegree = [0] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
  i, j = map(int, input().split())
  graph[i].append(j)
  indegree[j] += 1
que = deque()
#진입차수가 0인 node의 idx를 que에 저장
for i in range(1, n+1):
  if indegree[i] == 0:
    que.append(i)

result = []
while que:
  n = que.popleft()
  result.append(n)
  for v in graph[n]:
    indegree[v] -= 1
    if indegree[v] == 0:
      que.append(v)

print(*result)
