import sys
from collections import deque
input = sys.stdin.readline

row, column = map(int, input().split())
arr = []
que = deque()
beaver = deque()
visited = [[False] * column for _ in range(row)]
for i in range(row):
  tmp = list(map(str, input().strip()))
  for j in range(column):
    if tmp[j] == '*':
      tmp[j] = 0
      que.append([i, j])
    elif tmp[j] == 'S':
      tmp[j] = '.'
      beaver.append([i, j, 0])
    elif tmp[j] == 'D':
      tmp[j] = sys.maxsize
      goal = [i, j]
    elif tmp[j] == 'X':
      visited[i][j] = True

  arr.append(tmp)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while que:
  x, y = que.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<row and 0<=ny<column and arr[nx][ny] == ".":
      arr[nx][ny] = arr[x][y] + 1
      que.append([nx, ny])



flag = False
while beaver:
  # print(beaver)
  x, y, d = beaver.popleft()
  if [x, y] == goal:
    flag = True
    day = d
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<row and 0<=ny<column and not visited[nx][ny]:
       if arr[nx][ny] == '.' or arr[nx][ny] > d+1:
        visited[nx][ny] = True
        beaver.append([nx, ny, d+1])

if flag:
  print(day) 
else:
  print("KAKTUS")