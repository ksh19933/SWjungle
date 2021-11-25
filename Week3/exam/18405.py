import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, k = map(int, input().split())

arr = []
que = []
for i in range(n):
  tmp = list(map(int, input().split()))
  for j in range(n):
    if tmp[j] != 0:
      heappush(que, [0, tmp[j], i, j])
  arr.append(tmp)
t_time, x, y = map(int, input().split())
target = [x-1, y-1, t_time]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
while que:
  t, b, x, y = heappop(que)
  if x == target[0] and y == target[1]:
    print(b)
    exit(0)
  if t < target[2]:
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 0:
          heappush(que, [t+1, b, nx, ny])
          arr[nx][ny] = b

print(0)