import sys
from heapq import heappush, heappop
input = sys.stdin.readline

inf = sys.maxsize
city_num = int(input())
bus_num = int(input())

graph = [[] for _ in range(city_num+1)]

for _ in range(bus_num):
  i, j, c = map(int, input().split())
  graph[i].append([j, c])

start_city, destiantion = map(int, input().split())

heap = []
heappush(heap, [0, start_city])
distance = [inf] * (city_num + 1)
distance[start_city] = 0
while heap:
  cost, s = heappop(heap)
  if distance[s] < cost:
    continue

  for v, c in graph[s]:
    dist = cost + c
    if distance[v] > dist:
      distance[v] = dist
      heappush(heap, [distance[v], v])

print(distance[destiantion])
