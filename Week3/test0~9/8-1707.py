import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(n, id):
  global flag
  if id == -1:
    id = 1
  else:
    id = -1
  print(f'n, id: {n}, {id}')
  for i in gragh[n]:
    if not check[i]:
      check[i] = -id
      dfs(i, id)
    elif check[i] == check[n]:
      flag = 0
      return

n = int(input())

for _ in range(n):
  v_num, e_num = map(int, input().split())
  gragh = [[] for _ in range(v_num+1)]
  check = [False] * (v_num + 1)
  #그래프 생성
  for _ in range(e_num):
    i, j = map(int, input().split())
    gragh[i].append(j)
    gragh[j].append(i)
  flag = 1
  for i in range(1, v_num+1):
    if not check[i]:
      dfs(i, -1)
  print(check)
  if flag == 1:
    print("YES")
  else:
    print("NO")
