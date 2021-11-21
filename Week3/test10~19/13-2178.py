import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, move):
  global min_move
  if [x, y] == target:
    min_move = min(move+1, min_move)
    return
  que = deque([[x,y]])
  while que:
    i, j = que.popleft()
    for k in range(4):
      nx = i + dx[k]
      ny = j + dy[k]
      if 0 <= nx < x_target and 0<= ny < y_target  and arr[nx][ny] == 1:
        arr[nx][ny] = arr[i][j] + 1
        que.append([nx, ny])

x_target, y_target = map(int, input().split())

arr = [list(map(int, input().strip())) for _ in range(x_target)]

min_move = x_target * y_target
target = [x_target-1, y_target-1]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
bfs(0, 0, 1)
print(arr[x_target-1][y_target-1])