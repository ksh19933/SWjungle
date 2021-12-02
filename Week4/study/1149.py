import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
inf = sys.maxsize
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[inf] * 3 for _ in range(n)]
def dfs(cur, color, start):
    if cur == n -1:
        return arr[cur][color]
    if dp[cur][color] != inf:
        return dp[cur][color]
    for i in range(3):
        if i != color:       
           dp[cur][color] = min(dp[cur][color], dfs(cur+1, i, start) + arr[cur][color])
    return dp[cur][color]
for i in range(3):
    dfs(0, i, i)
print(min(dp[0]))



import sys
input = sys.stdin.readline

if __name__=='__main__':
    num_house = int(input().strip())

    costs = [list(map(int, input().split())) for _ in range(num_house)]

    # dp[i][j] == i번째 집이 j색(R:0, G:1, B:2)을 고를 때, 그때까지의 최소 비용
    dp = [[0]*3 for _ in range(num_house)]

    dp[0] = costs[0]
    for i in range(1, num_house):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]

    print(min(dp[num_house-1][0], dp[num_house-1][1], dp[num_house-1][2]))