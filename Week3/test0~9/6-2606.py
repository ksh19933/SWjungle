import sys
input = sys.stdin.readline
def dfs(n):
  global cnt 
  cnt += 1
  visited[n] = True
  for i in gragh[n]:
    if not visited[i]:
      dfs(i)

computer_num = int(input())
m = int(input())
gragh = [[] for _ in range(computer_num + 1)]
visited = [False] * (computer_num + 1)
# 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

for _ in range(m):
  i, j = map(int, input().split())
  gragh[i].append(j)
  gragh[j].append(i)

cnt = -1
dfs(1)
print(cnt)
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7