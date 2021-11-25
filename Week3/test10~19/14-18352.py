import sys
from collections import deque
input = sys.stdin.readline

city_num, road_num, road_info, start_city = list(map(int, input().split()))

graph = [[] for _ in range(city_num+1)]

for _ in range(road_num):
  i, j = list(map(int, input().split()))
  graph[i].append(j)

que = deque([[start_city, 0]])
visited = [False] * (city_num + 1)
stack = []
while(que):
  n, leng = que.popleft()
  visited[n] = True
  if leng == road_info:
    stack.append(n)
  for v in graph[n]:
    if not visited[v]:
      que.append([v, leng + 1])

if stack:
  stack.sort()
  for i in range(len(stack)):
    print(stack[i])
else:
  print(-1)