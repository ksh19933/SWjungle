import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
que = deque()
indegree = [0] * (n+1)
for _ in range(m):
  i, j, k = map(int, input().split())
  graph[j].append([i, k])
  indegree[i] += 1

for i in range(1, n+1):
  if indegree[i] == 0:
    que.append(i)

needs = [[0] * (n+1) for _ in range(n+1)]

while que:
  idx = que.popleft()
  for part, num in graph[idx]:
    #기본 부품일 일 경우 needs[part][idx]에 바로 더해준다
    #count(0) == N+1 로 확인 ==> 기본 부품이 아닐경우 0이 외의 숫자가 존재하므로 count(0)는 N+1이 아니다
    if needs[idx].count(0) == n+1:
      needs[part][idx] += num
    else:
      for i in range(1, n+1):
        needs[part][i] += needs[idx][i] * num
    indegree[part] -= 1
    if indegree[part] == 0:
      que.append(part)

for i in range(1, n+1):
  if needs[n][i] != 0:
    print(f'{i} {needs[n][i]}')




# import sys
# from collections import deque
# input = sys.stdin.readline

# def dfs(n):
#   if graph[n] == []:
#     result[n] += 1
#     return
#   for v in graph[n]:
#       dfs(v)

# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#   i, j, k = map(int, input().split())
#   for _ in range(k):
#     graph[i].append(j)


# result = [0] * (n+1)

# dfs(n)

# for i in range(1, n+1):
#   if result[i] != 0:
#     print(f'{i} {result[i]}')

