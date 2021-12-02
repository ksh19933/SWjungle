import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
stack = []
dp = [0] * n
for i in range(n):
    idx = bisect_left(stack, arr[i])
    if len(stack) <= idx:
        stack.append(arr[i])
    else:
        stack[idx] = arr[i]
    dp[i] = idx+1
arr.reverse()
stack = []
for i in range(n):
    idx = bisect_left(stack, arr[i])
    if len(stack) <= idx:
        stack.append(arr[i])
    else:
        stack[idx] = arr[i]
    dp[n-i-1]= dp[n-i-1] + idx
print(max(dp))