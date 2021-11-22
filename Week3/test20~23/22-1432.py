import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
outdegree = [0] * (n+1)
for i in range(1, n+1):
  tmp = list(map(int, input().strip()))
  for j in range(1, n+1):
    if tmp[j-1] == 1:
      graph[j].append(i)
      outdegree[i] += 1

que = []
for i in range(1, n+1):
  if outdegree[i] == 0:
    heappush(que, -i)

if que == []:
  print(-1)
else:
  result = [0] * (n+1) #[i for i in range(n+1)]
  i = n+1
  while que:
    i -= 1
    idx = -heappop(que)
    result[idx] = i
    for v in graph[idx]:
      outdegree[v] -= 1
      if outdegree[v] == 0:
        heappush(que, -v)
  for i in range(1, n+1):
    print(result[i], end= ' ')

# import sys
# input = sys.stdin.readline

# n = int(input())

# graph = [[] for _ in range(n+1)]
# outdegree = [0] * (n+1)
# for i in range(1, n+1):
#   tmp = list(map(int, input().strip()))
#   for j in range(1, n+1):
#     if tmp[j-1] == 1:
#       graph[j].append(i)
#       outdegree[i] += 1

# que = []
# for i in range(1, n+1):
#   if outdegree[i] == 0:
#     que.append(i)

# if que == []:
#   print(-1)
# else:
#   result = [0] * (n+1) #[i for i in range(n+1)]
#   i = n+1
#   while que:
#     que.sort()
#     i -= 1
#     idx = que.pop()
#     result[idx] = i
#     for v in graph[idx]:
#       outdegree[v] -= 1
#       if outdegree[v] == 0:
#         que.append(v)
#   for i in range(1, n+1):
#     print(result[i], end= ' ')    