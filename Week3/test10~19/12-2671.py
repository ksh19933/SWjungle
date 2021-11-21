import sys
input = sys.stdin.readline

def dfs(n, depth, graph):
  check[n] = True
  for i in graph[n]:
    if not check[i]:
      depth = dfs(i, depth+1, graph)
  # print(depth)
  return depth

n, m = map(int, input().split())

graph_max = [[] for _ in range(n+1)]
graph_min = [[] for _ in range(n+1)]
for _ in range(m):
  i, j = map(int, input().split())
  graph_max[j].append(i)
  graph_min[i].append(j)

mid = n//2
result = 0
for i in range(1, n+1):
  check = [False] * (n+1)
  depth = dfs(i, 0, graph_max)
  if mid < depth:
    result += 1
  check = [False] * (n+1)
  depth = dfs(i, 0, graph_min)
  if mid < depth:
    result += 1


print(result)

