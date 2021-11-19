# import sys

# n = int(sys.stdin.readline())
# STRING = [sys.stdin.readline().strip() for _ in range(n)]
# for string in STRING:
#   key_location = 0
#   temp_password = []
#   for s in string:
#     if s == "<":
#       if key_location > 0:
#         key_location -= 1
#     elif s == ">":
#       if key_location < len(temp_password):
#         key_location += 1
#     elif s == "-":
#       if temp_password and key_location > 0:
#         temp_password.pop(key_location-1)
#         key_location -= 1
#     else:
#       temp_password.insert(key_location, s)
#       key_location += 1 
#   print(''.join(temp_password))

import sys
n = int(sys.stdin.readline())
for _ in range(n):
  string = sys.stdin.readline().strip()
  left , right = [], []
  for s in string:
    if s == "<":
      if left:
        right.append(left.pop())
    elif s == ">":
      if right:
        left.append(right.pop())
    elif s == "-":
      if left:
        left.pop()
    else:
      left.append(s)
  print(''.join(left) + ''.join(right[::-1]))
