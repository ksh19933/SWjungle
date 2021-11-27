import sys
input = sys.stdin.readline
n = int(input())

arr = []
for _ in range(n):
    i, j = map(int, input().split())
    arr.append([i, j])

arr.sort()
stack = [arr[0]]
cnt = 1
print(arr)
for i in range(1, n):
    if arr[i][1] < stack[-1][1]:
        stack.pop()
        stack.append(arr[i])
    elif stack[-1][1] <= arr[i][0]:
        stack.append(arr[i])
        cnt += 1
    print(stack)
print(cnt)