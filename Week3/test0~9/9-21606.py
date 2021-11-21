import sys
sys.setrecursionlimit(10**9)
#dfs 함수 선언
def dfs(n):
  global cnt
  for i in gragh[n]:
    if not check[i]:
      check[i] = -1
      dfs(i)
#조건 1 넘어간 지역이 실외 일것
    elif check[i] == 1:
      cnt += 1
#넘어간 후 실내일 경우 산책 종료

##input 받기
input = sys.stdin.readline
node_num = int(input())
check = [0] + list(map(int, input().strip()))
gragh = [[] for _ in range(node_num + 1)]

for _ in range(node_num-1):
  i, j = map(int, input().split())
  gragh[i].append(j)
  gragh[j].append(i)
result = 0
#모든 점에서부터 산책을 시작한다.
for start in range(1, node_num+1):
  if check[start] == 0:
    cnt = 0
    check[start] = -1
    dfs(start)
    result += cnt * (cnt-1)
  elif check[start] == 1:
    #실내끼리 연결되 있을 경우
    for v in gragh[start]:
      if check[v] == 1:
        result += 1
print(result)