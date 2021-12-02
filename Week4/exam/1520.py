# import sys
# from heapq import heappush, heappop
# input = sys.stdin.readline
# r, c = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(r)]
# dp = [[0] * c for _ in range(r)]
# dp[0][0] = 1
# que = []
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# heappush(que, [-arr[0][0], 0, 0])
# while que:
#     h, x, y = heappop(que)
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<=nx<r and 0<=ny<c and arr[x][y] > arr[nx][ny]:
#             if dp[nx][ny] == 0:
#                 heappush(que, [-arr[nx][ny], nx, ny])
#             dp[nx][ny] += dp[x][y]
# print(dp[-1][-1])

import sys
input = sys.stdin.readline

def dfs(x, y):
    if [x , y] == [r-1, c-1]:
        return dp[x][y]
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<r and 0<=ny<c and arr[x][y] > arr[nx][ny]:
            dp[x][y] += dfs(nx,ny)
    return dp[x][y]

r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
dp = [[-1] * c for _ in range(r)]
dp[-1][-1] = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
print(dfs(0,0))