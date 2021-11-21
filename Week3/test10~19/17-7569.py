import sys
from collections import deque
input = sys.stdin.readline

def bfs():
  ##que에서 빼내면서 1 주위에  숫자들을 +1로 바꿔준다.
  while que:
    z, x, y = que.popleft()
    for k in range(6):
      nz = z + dz[k] 
      nx = x + dx[k]
      ny = y + dy[k]
      if 0<=nz<h and 0<=nx<n and 0<=ny<m and arr[nz][nx][ny] == 0:
        arr[nz][nx][ny] = arr[z][x][y] + 1
        que.append([nz, nx, ny])

m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

que = deque()
for z in range(h):
  for i in range(n):
    for j in range(m):
      if arr[z][i][j] == 1:
        que.append([z, i, j])

bfs()
flag = 0
day = 0
for z in range(h):
  if flag == 1:
    break
  for i in range(n):
    if flag == 1:
      break
    for j in range(m):
      if arr[z][i][j] == 0:
        flag = 1
        break
      day = max(day, arr[z][i][j])

if flag == 1:
  print(-1)
else:
  print(day-1)

#value를 다른곳에 저장함으로써 시간을 단축할 수 있음
