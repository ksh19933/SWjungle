import sys
input = sys.stdin.readline

def bfs(i, j):
  que = [[i,j]]
  apart_num = 0
  while que:
    apart_num += 1
    x, y = que.pop()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0<= ny < n and arr[nx][ny] == 1:
        arr[nx][ny] = -1
        que.append([nx, ny])
  return apart_num

n = int(input())

arr = [list(map(int, input().strip())) for _ in range(n)]

cnt = 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
result = []
for i in range(n):
  for j in range(n):
    if arr[i][j] == 1:
      arr[i][j] = -1
      apart_num = bfs(i, j)
      cnt += 1
      result.append(apart_num)

result.sort()
print(cnt)
for r in result:
  print(r)