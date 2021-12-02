import sys
from collections import deque
input = sys.stdin.readline
test_num = int(input())
for _ in range(test_num):
    n, e = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for _ in range(e):
        i , j = map(int, input().split())
        graph[i].append(j)
        indegree[j] += 1
    target = int(input())
    que = deque()
    dp = [0] * (n+1)
    for i in range(1, n+1):
        if indegree[i] == 0:
            que.append(i)
            dp[i] = time[i]

    while que:
        i = que.popleft()
        for v in graph[i]:
            dp[v] = max(dp[v], dp[i] + time[v])
            indegree[v] -= 1
            if indegree[v] == 0:
                que.append(v)
    print(dp[target])