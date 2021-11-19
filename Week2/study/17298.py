# import sys
# n = int(sys.stdin.readline())
# num_list = list(map(int, sys.stdin.readline().split()))
# stack = []
# result = [-1] * n
# for i in range(n-1, -1, -1):
#   while stack:
#     if num_list[stack[-1]] <= num_list[i]:
#       stack.pop()
#     else:
#       result[i] = num_list[stack[-1]]
#       break
#   stack.append(i)

# print(*result)


import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
stack = []
result = [-1] * n
for i in range(n):
  while stack and num_list[stack[-1]] <= num_list[i]:
      result[stack.pop()] = num_list[i]
  stack.append(i)

print(*result)
