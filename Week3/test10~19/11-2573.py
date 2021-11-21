import sys
from collections import deque
input = sys.stdin.readline
def iceberg(x, y):
  que = deque([[x, y]])
  check[x][y] = True
  melt = deque()
  while que:
    melt_cnt = 0
    i, j = que.popleft()
    for k in range(4):
      nx = i + dx[k]
      ny = j + dy[k]
      if arr[nx][ny] != 0 and not check[nx][ny]:
        que.append([nx, ny])
        check[nx][ny] = True
      elif arr[nx][ny] == 0:
        melt_cnt += 1
    if melt_cnt:
      melt.append([i, j, melt_cnt])
  return melt

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

r, c = map(int, input().split())

arr = []

for i in range(r):
  arr.append(list(map(int, input().split())))


year = 0
while True:
  flag = 0
  check = [[False]*c for _ in range(r)]
  for i in range(1, r-1):
    for j in range(1, c-1):
      if arr[i][j] != 0 and not check[i][j]:  
        melt = iceberg(i, j)
        flag += 1
        while melt:
          x, y, cost = melt.popleft()
          arr[x][y] = max(0, arr[x][y]-cost)
  if flag == 0:
    year = 0
    break
  elif flag > 1:
    break
  year += 1

print(year)



# def melt():
#   arr_copy = copy.deepcopy(arr)
#   for j in range(1, r-1):
#     for k in range(1,c-1):
#       if arr[j][k] != 0:
#         for i in range(4):
#           nx = j + dx[i]
#           ny = k + dy[i]
#           if arr[nx][ny] == 0:
#             arr_copy[j][k] -= 1

#       if arr_copy[j][k] < 0:
#         arr_copy[j][k] = 0

#   return arr_copy

# def check_init():
#   check = [[False]*c for _ in range(r)]
#   for i in range(r):
#     for j in range(c):
#       if arr[i][j] != 0:
#         check[i][j] = True
#   return check