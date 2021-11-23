import sys
from collections import deque
input = sys.stdin.readline

case_num = int(input())
for _ in range(case_num):
  building_num, construction_order = map(int, input().split())

  cost = [0] + list(map(int, input().split()))

  graph = [[] for _ in range(building_num+1)]
  indegree = [0] * (building_num+1)
  for _ in range(construction_order):
    i, j = map(int, input().split())
    graph[i].append(j)
    indegree[j] += 1

  target = int(input())
  dp = [0] * (building_num+1)
  for i in range(len(cost)):
    dp[i] = cost[i]
  que = deque()
  for i in range(1, building_num+1):
    if indegree[i] == 0:
      que.append(i)
  while que:
    n = que.popleft()
    for v in graph[n]:
      dp[v] = max(dp[v], dp[n] + cost[v])
      indegree[v] -= 1
      if indegree[v] == 0:
        que.append(v)
  print(dp[target])