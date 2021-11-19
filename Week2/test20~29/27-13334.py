import sys
import heapq

n = int(sys.stdin.readline())

point_all = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

d = int(sys.stdin.readline())
points = []
for point in point_all:
  if abs(point[1] - point[0]) <= d:
    points.append(sorted(point))

points.sort(key=lambda x:x[1])
heap_points = []
max_num = 0
for point in points:
  if not heap_points:
    heapq.heappush(heap_points, point)
  else:
    ## heap의 0번부터 n-1번까지 len(heap)
    while heap_points[0][0] < point[1] - d:
      heapq.heappop(heap_points)
      if not heap_points:
        break
    heapq.heappush(heap_points, point)
  
  max_num = max(max_num, len(heap_points))

print(max_num)