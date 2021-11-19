# import sys

# while True:
#   test_case = list(map(int, sys.stdin.readline().split()))
#   n = test_case.pop(0)
#   if n == 0:
#     break
#   max_area = 0
#   change_length_idx = [0]
#   for i in range(1, n):
#     if test_case[i-1] != test_case[i]:
#       change_length_idx.append(i)

#   for idx in change_length_idx:
#     area = 0
#     for i in range(idx, len(test_case)):
#       if test_case[idx] <= test_case[i]:
#         area += test_case[idx]
#       else: #test_case[idx] < test_case[i]
#         break
#     if area >= max_area:
#       max_area = area
#   print(max_area)





# import sys

# def segment_area(height_list):
#   global max_area
#   if len(height_list) == 1:
#     # print(f'area: {height_list[0]}')
#     if height_list[0] > max_area:
#       max_area = height_list[0]
#     return
#   # print(f'height_list: {height_list}')  
#   min_height = min(height_list)
#   area = min_height * len(height_list)

#   if area > max_area:
#     max_area = area
#   # print(f'area: {area}')
#   min_idx = height_list.index(min_height)
#   # print(f'min_idx: {min_idx}')
#   if min_idx == 0:
#     segment_area([height_list[min_idx]])
#     segment_area(height_list[min_idx+1:])
#   elif min_idx == (len(height_list)-1):
#     segment_area(height_list[:min_idx])
#     segment_area([height_list[min_idx]])
#   else:
#     segment_area(height_list[:min_idx])
#     segment_area(height_list[min_idx+1:])


# while True:
#   height_list = list(map(int, sys.stdin.readline().split()))
#   n = height_list.pop(0)
#   if n == 0:
#     break
#   max_area = 0
#   segment_area(height_list)
#   print(max_area)


# import sys

# def segment_area(height_list):
#   global max_area
#   if len(height_list) == 1:
#     # print(f'area: {height_list[0]}')
#     if height_list[0] > max_area:
#       max_area = height_list[0]
#     return
#   # print(f'height_list: {height_list}')  
#   min_height = min(height_list)
#   area = min_height * len(height_list)

#   if area > max_area:
#     max_area = area
#   # print(f'area: {area}')
#   min_idx = height_list.index(min_height)
#   # print(f'min_idx: {min_idx}')
#   if min_idx == 0:
#     segment_area([height_list[min_idx]])
#     segment_area(height_list[min_idx+1:])
#   elif min_idx == (len(height_list)-1):
#     segment_area(height_list[:min_idx])
#     segment_area([height_list[min_idx]])
#   else:
#     segment_area(height_list[:min_idx])
#     segment_area(height_list[min_idx+1:])


# while True:
#   height_list = list(map(int, sys.stdin.readline().split()))
#   n = height_list.pop(0)
#   if n == 0:
#     break
#   max_area = 0
#   segment_area(height_list)
#   print(max_area)

import sys

def segment_area(left, right):
  if left == right:
    return height_list[left]
  
  mid = (left + right) // 2
  temp_max = max(segment_area(left, mid),segment_area(mid+1, right))
  mid_to_left = mid
  mid_to_right = mid+1
  min_height = min(height_list[mid_to_left], height_list[mid_to_right])
  temp_max = max(temp_max, min_height*2)

  while( left < mid_to_left or mid_to_right < right):
    print(mid_to_left, mid_to_right)
    if mid_to_right < right and (left == mid_to_left or height_list[mid_to_left -1] < height_list[mid_to_right+1]):
      mid_to_right += 1
      min_height = min(min_height, height_list[mid_to_right])
    else: #mid_to_right >= right or (left != mid_to_left and height_list[mid_to_left -1] >= height_list[mid_to_right+1]):
      mid_to_left -= 1
      min_height = min(min_height, height_list[mid_to_left])

    temp_max = max(temp_max, min_height*(mid_to_right-mid_to_left + 1))
  return temp_max

while True:
  height_list = list(map(int, sys.stdin.readline().split()))
  n = height_list.pop(0)
  if n == 0:
    break
  max_area = segment_area(0, n-1)
  print(max_area)



