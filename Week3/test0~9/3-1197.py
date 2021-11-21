# 특정 원소가 속한 집합을 찾기
def find(parent, x):
  if parent[x] == x:
    return x
  else: 
    y = find(parent, parent[x])
    return y
# 두 원소가 속한 집합을 합치기 (간선 연결한다고 생각!)
def union(parent, a, b):
  root_a = find(parent, a)
  root_b = find(parent, b)
  if root_a < root_b:
    parent[root_b] = root_a
  else:
    parent[root_a] = root_b

import sys

input = sys.stdin.readline
# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [i for i in range(v+1)]
edges = []
result = 0

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 오름차순 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
  # 사이클이 발생하지 않는 경우에만 집합에 포함(=연결한다.)
  cost, a, b = edge
  if find(parent, a) != find(parent, b):
    union(parent, a,b)
    result += cost
print(result)

print(parent)







# import sys

# v, e = map(int, sys.stdin.readline().split())

# weight_list = [[1000001] * v for _ in range(v)] #weight[i][j] 는 i -> j 일 때 드는 가중치

# visited = [False] * v

# weights = [1000001] * v

# for _ in range(e):
#   i, j, w = map(int, sys.stdin.readline().split())
#   weight_list[i-1][j-1] = w

# #get_min_node
# def get_min_node(v):
#   #해당 노드를 방문했는지 확인
#   for i in range(v):
#     if not visited[i]:
#       min = i
#       break
#   #아직 방문하지 않지만 위에서 발견한 노드보다 weight가 낮은 노드를 찾는다.
#   for i in range(v):
#     if not visited[i] and weights[i] < weights[min]:
#       min  = i
#   return min


# #프림 알고리즘
# def prim(start, node_num):
#   #시작 노드의 distance를 0으로 초기화
#   weights[start] = 0
#   ##알고리즘 시작
#   for _ in range(node_num):
#     #연결되어 있는 노드 사이의 최소인 가중치를 가지고 있는 노드를 찾는다.
#     node = get_min_node(node_num)
#     visited[node] = True
#     for j in range(node_num):
#       #위에서 찾는 노드와 연결되어 있는 간선의 최소 가중치를 찾는다
#       if weight_list[node][j] != 1000001:
#         if not visited[j] and weights[j] > weight_list[node][j]:
#           #그 중 weights가 최소인 노드와 연결한다.
#           weights[j] = weight_list[node][j]

#   return sum(weights) 

# print(prim(0, v))


