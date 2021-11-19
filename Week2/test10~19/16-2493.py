# import sys

# def height_check(left, right, height):
#   if left == right:
#     if height < lazer_tower_height[left]:
#       return right
#     else:
#       return -1
  
#   mid = (left + right) // 2
#   # print(f'left, mid, right: {left}, {mid}, {right}')
#   if lazer_tower_height[mid+1] > height:
#     max_idx = height_check(mid+1, right, height)
#   else:
#     max_idx = max(height_check(left, mid, height), height_check(mid+1, right, height))

#   return max_idx



# tower_num = int(sys.stdin.readline())
# lazer_tower_height = list(map(int, sys.stdin.readline().split()))

# receive_location = []
# for i in range(tower_num-1, -1, -1):
#   receive_location.append(height_check(0, i, lazer_tower_height[i]))

# for i in range(tower_num-1, -1, -1):
#   print(receive_location[i]+1, end= ' ')



import sys

tower_num = int(sys.stdin.readline())
lazer_tower_height = list(map(int, sys.stdin.readline().split()))
stack = []
recieve_location = [0] * tower_num
for i in range(tower_num):
  while len(stack) != 0:
    #stack의 top에 있는 height보다 크거나 같으면 top을 pop시킨다.
    if stack[-1][1] <= lazer_tower_height[i]:
      stack.pop()
    else:
    #stack의 top에 있는 height보다 작으면 stack에 추가한다(이때  top에 저장되어있는 위치 정보를 recieve_location에 저장한다.).
      recieve_location[i] = stack[-1][0] + 1
      break
  
  stack.append([i,lazer_tower_height[i]])

print(*recieve_location)



import sys

tower_num = int(sys.stdin.readline())
lazer_tower_height = list(map(int, sys.stdin.readline().split()))
stack = []
recieve_location = [0] * tower_num
for i in range(tower_num):
  while stack:
    #stack의 top에 있는 height보다 크거나 같으면 top을 pop시킨다.
    if lazer_tower_height[stack[-1]] <= lazer_tower_height[i]:
      stack.pop()
    else:
    #stack의 top에 있는 height보다 작으면 stack에 추가한다(이때  top에 저장되어있는 위치 정보를 recieve_location에 저장한다.).
      recieve_location[i] = stack[-1] + 1
      break
  
  stack.append(i)

print(*recieve_location)