from bisect import bisect_left
import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0] * (n)
dp[0] = 1
stack = [arr[0]]
for i in range(1, n):
    if stack[-1] < arr[i]:
        stack.append(arr[i])
        dp[i] = len(stack)
    else:
        idx = bisect_left(stack, arr[i])
        dp[i] = idx + 1
        stack[idx] = arr[i]
print(dp)
maxval = len(stack)
print(maxval)
result = []
for i in range(n-1, -1, -1):
    if dp[i] == maxval:
        result.append(arr[i])
        maxval -= 1

print(*result[::-1])