def solution(n, computers):
    answer = 0
    visited = [False] * n
    def bfs(idx):
        visited[idx] = True
        que = [idx]
        while que:
            v = que.pop()
            for i in range(n):
                if not visited[i] and computers[v][i]:
                    visited[i] = True
                    que.append(i)
        return 1
    for i in range(n):
        if not visited[i]:
            answer += bfs(i)
    return answer