import sys
sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline())

def DFS(x):
    global flag
    print(x, visited[x])
    for adj in graph[x]:
        if visited[adj] == 0:
            visited[adj] = -visited[x]
            DFS(adj)
        elif visited[adj] == visited[x]:
            flag = False
            return

for i in range(n):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for i in range(v+1)]
    visited = [0] * (v+1)
    for i in range(e):
      a, b=  map(int, sys.stdin.readline().split())
      graph[a].append(b)
      graph[b].append(a)

    flag = True    
    for node in range(1, v+1):
        if visited[node] == 0:
            visited[node] = 1
            DFS(node)
    print(visited)
    if flag == True:
        print("Yes")
    else:
        print("NO")

