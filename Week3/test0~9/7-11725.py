import sys

sys.setrecursionlimit(10**9)
def dfs(n):
  for i in gragh[n]:
    if parent[i] == 0:
      parent[i] = n
      dfs(i)


n = int(sys.stdin.readline())
gragh = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
  i, j = map(int, sys.stdin.readline().split())
  gragh[i].append(j)
  gragh[j].append(i)

print(gragh)
dfs(1)

# print(gragh)
# print(parent)
for i in range(2, n+1):
  print(parent[i])