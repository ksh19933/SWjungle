# import sys

# n = int(sys.stdin.readline())
# stack = [0] * (1000)
# for i in range(n):
#   arr = list(map(int,sys.stdin.readline().split()))
#   for i in range(arr[0], arr[2]):
#     if stack[i] < arr[1]:
#       stack[i] = arr[1]

# changed_height = 0
# for i in range(len(stack)):
#   if changed_height != stack[i]:
#     changed_height = stack[i]
#     print(f'{i} {stack[i]}', end=' ')


# import sys
# import heapq

# n = int(sys.stdin.readline())
# arr = []

# for i in range(n):
#   a = list(map(int, sys.stdin.readline().split()))
#   arr.append([a[0], a[1], 0])
#   arr.append([a[2], a[1], 1])
# arr.sort()
# heap =[]
# ans = []
# max_height = 0
# for a in arr:
#   if not heap:
#     heapq.heappush(heap, (-a[1], a))
#     max_height = a[1]
#     ans.append([a[0], a[1]])
#     continue
#   if a[2] == 1:
#     temp = []
#     while True:
#       temp_arr = heapq.heappop(heap)
#       if temp_arr[1][1] == a[1]:
#         while temp:
#           heapq.heappush(heap, heapq.heappop(temp))
#         break
#       temp.append(temp_arr)
#     if not heap:
#       ans.append([a[0], 0])
#     elif max_height != heap[0][1][1]:
#       ans.append([a[0], heap[0][1][1]])
#       max_height = heap[0][1][1]
#   else:
#     heapq.heappush(heap, (-a[1], a))
#     if max_height != heap[0][1][1]:
#       ans.append([heap[0][1][0], heap[0][1][1]])
#       max_height = heap[0][1][1]
#   #점을 없앴는데 stack이 빌 경우 최대 높이를 0으로 설정


# for a in ans:
#   print(*a, end= ' ')

# import sys

# n = int(sys.stdin.readline())
# arr = []

# for i in range(n):
#   a = list(map(int, sys.stdin.readline().split()))
#   arr.append([a[0], a[1], 0])
#   arr.append([a[2], a[1], 1])

# arr.sort()
# stack =[]
# ans = []
# max_height = 0
# for a in arr:
#   if not stack:
#     stack.append(a)
#     max_height = a[1]
#     ans.append([a[0], a[1]])
#     continue
#   if a[2] == 1:
#     for i in range(len(stack)):
#       if stack[i][1] == a[1]:
#         stack.pop(i)
#         break
#     if not stack:
#       ans.append([a[0], 0])
#       max_height = 0
#     else:
#       if a[1] == max_height:
#         temp_height = 0
#         for i in range(len(stack)):
#           if stack[i][1] > temp_height:
#             temp_height = stack[i][1]
#         max_height = temp_height
#         ans.append([a[0], max_height])
#   else:
#     stack.append(a)
#     if max_height < stack[-1][1]:
#       ans.append([stack[-1][0], stack[-1][1]])
#       max_height = stack[-1][1]
# for a in ans:
#   print(*a, end= ' ')

import sys
import heapq

n = int(sys.stdin.readline())
arr = []

for i in range(n):
  a = list(map(int, sys.stdin.readline().split()))
  arr.append([a[0], a[2], a[1]])
arr.sort()
heap = []
ans = []
i, n = 0, len(arr)
while i < n or heap:
  #heap이 비었을 때 혹은 최대 넓이의 오른쪽 좌표가 arr[i]의 왼쪽 좌표보다 클 때 heappush
  if not heap or i < n and arr[i][0] <= -heap[0][1]:
    temp = arr[i][0]
    while i <  n and arr[i][0] == temp:
      heapq.heappush(heap, (-arr[i][2], -arr[i][1]))
      i += 1
  #arr[i]의 왼쪽좌표가 heap[0]의 오른쪽 좌표보다 클 때
  else:
    temp = -heap[0][1]
    while heap and -heap[0][1] <= temp:
      heapq.heappop(heap)
      
  print(heap)
  if heap: 
    height = -heap[0][0]
  else:
    height = 0
  # print(f'temp, height: {temp}, {height}')
  if not ans or height != ans[-1][1]:
    ans.append([temp, height])

for a in ans:
  print(*a, end= ' ')



# import sys
# import heapq

# n = int(sys.stdin.readline())
# arr = []

# for i in range(n):
#   a = list(map(int, sys.stdin.readline().split()))
#   arr.append([a[0], a[2], a[1]])
# arr.sort()
# heap = []
# ans = []
# i, n = 0, len(arr)
# for a in arr:
#   #heap이 비었을 때 혹은 최대 넓이의 오른쪽 좌표가 arr[i]의 왼쪽 좌표보다 클 때 heappush
#   if not heap or a[0] <= -heap[0][1]:
#     temp = a[0]
#     heapq.heappush(heap, (-a[2], -a[1]))
#   #arr[i]의 왼쪽좌표가 heap[0]의 오른쪽 좌표보다 클 때
#   else:
#     temp = -heap[0][1]
#     while heap and -heap[0][1] <= temp:
#       heapq.heappop(heap)

#   print(heap)

#   # height = len(heap) and -heap[0][0]
#   if heap:
#     height = -heap[0][0]
#   else:
#     height = 0
#   # print(f'temp, height: {temp}, {height}')
#   if not ans or height != ans[-1][1]:
#     ans.append([temp, height])

# for a in ans:
#   print(*a, end= ' ')