# import sys


# string_length, arr_length = map(int, sys.stdin.readline().split())

# num = list(map(int, sys.stdin.readline().strip()))
# stack = [num[i] for i in range(string_length - arr_length)]

# min_num = min(stack)

# for i in range(string_length - arr_length, string_length):
#   j = 0
#   while(stack[j] != min_num):
#     # print(f'j, stack[j]: {j}, {stack[j]}')
#     j += 1
#   stack.pop(j)
#   stack.append(num[i])
#   min_num = min(stack)

# for _ in range(len(stack)):
#   print(stack[_], end='')



import sys

string_length, k = map(int, sys.stdin.readline().split())
remove_num = k
num = list(map(int, sys.stdin.readline().strip()))
stack = []
for i in range(string_length):
  while (remove_num > 0 and stack and stack[-1] < num[i]):
    stack.pop()
    remove_num -= 1
  stack.append(num[i])

print(stack)
for i in range(string_length-k):
  print(stack[i], end='')