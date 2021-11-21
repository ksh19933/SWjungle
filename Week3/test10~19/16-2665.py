import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def bfs(x, y, clear):
  heap = []
  heappush(heap , [clear, x, y])
  while heap:
    c, x, y = heappop(heap)
    if [x, y] == destination:
      return c
    if visited[x][y]:
      continue
    visited[x][y] = True
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<= nx < n and 0<= ny < n and not visited[nx][ny]:
        if arr[nx][ny] == 1:
          heappush(heap, [c, nx, ny])
        elif arr[nx][ny] == 0:
          heappush(heap, [c+1, nx, ny])
  
n = int(input())
destination = [n-1, n-1]
arr = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
print(bfs(0, 0, 0))

