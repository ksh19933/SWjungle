import sys
from collections import deque
input = sys.stdin.readline

city_num = int(input())
road_num = int(input())
graph = [[] for _ in range(city_num+1)]
back_graph = [[] for _ in range(city_num+1)]
result = [0] * (city_num + 1)
indegree = [0] * (city_num+ 1)
for _ in range(road_num):
  i, j, c = map(int, input().split())
  graph[i].append([j, c])
  back_graph[j].append([i, c])
  indegree[j] += 1
start_city, end_city = map(int, input().split())

que = deque()
que.append(start_city)

while que:
  n = que.popleft()
  for v, c in graph[n]:
    indegree[v] -= 1
    result[v] = max(result[v], result[n]+c)
    if indegree[v] == 0:
      que.append(v)
print(back_graph)
visited = [False] * (city_num +1)
que.append(end_city)
cnt = 0
while que:
  n = que.popleft()
  for v, c in back_graph[n]:
    if result[n] - result[v] == c:
      cnt += 1
      #중복 제거
      if not visited[v]:
        visited[v] = True
        que.append(v)

print(result[end_city])
print(cnt)