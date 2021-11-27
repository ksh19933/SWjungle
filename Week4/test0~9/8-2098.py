import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = sys.maxsize
#무엇을 리턴?
#dp 값
def dfs(current, visit):
    ##마지막에 도달
    if visit == (1<<n) -1:
        if arr[current][0] == 0:
            return inf
        else:
            return arr[current][0]
    
    #dp값이 존재할 경우
    if dp[current][visit] != inf:
        return dp[current][visit]

    #방문했음을 어떻게 표현? -> not visit & (1<<i)
    #current -> i  로 이동이 가능해야함
    #[current][i] = current에서 i로 이동
    for i in range(n):
        if not visit & (1<<i) and arr[current][i] != 0:
            dp[current][visit] = min(dp[current][visit], dfs(i, visit | (1<<i)) + arr[current][i])
    
    return dp[current][visit]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[inf] * (1<<n) for _ in range(n)]
print(dfs(0, 1))

    