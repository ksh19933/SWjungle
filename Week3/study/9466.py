import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(i, que):
  global result
  visited[i] = True
  que.append(i)
  v = graph[i]
  if visited[v]:
    if v in que:
      result += que[que.index(v):]
  else:
    dfs(v, que)

case_num = int(input())

for _ in range(case_num):
  student_num = int(input())
  graph = [0] + list(map(int, sys.stdin.readline().split()))
  result = []
  visited = [False] * (student_num+1)
  for i in range(1, student_num+1):
    if not visited[i]:
      dfs(i, [])
  print(student_num - len(result))