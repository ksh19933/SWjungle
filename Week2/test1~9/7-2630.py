# import sys
# def paper_cut(x_start, y_start, length):
#   global white_num
#   global blue_num
#   if length == 0:
#     if squre[0][0] == 1:
#       blue_num += 1
#     else:
#       white_num += 1
#     return
#   quadrant1 = []
#   quadrant2 = []
#   quadrant3 = []
#   quadrant4 = []

#   for i in range(length):
#     quadrant1.append(squre[i][:length])
#     quadrant2.append(squre[i+length][:length])
#     quadrant3.append(squre[i][length:])
#     quadrant4.append(squre[i+length][length:])
  
#   if color_check(quadrant1, length) == 1:
#     pass
#   else:
#     paper_cut(quadrant1, length//2)

#   if color_check(quadrant2, length) == 1:
#     pass
#   else:
#     paper_cut(quadrant2, length//2)

#   if color_check(quadrant3, length) == 1:
#     pass
#   else:
#     paper_cut(quadrant3, length//2)

#   if color_check(quadrant4, length) == 1:
#     pass
#   else:
#     paper_cut(quadrant4, length//2)  



# def color_check(squre, length):
#   num_sum = 0
#   global white_num
#   global blue_num
#   for i in range(length):
#     num_sum += sum(squre[i])
#   if num_sum == 0:
#     white_num += 1
#     return 1
#   elif num_sum == squre[0][0]*(length*length):
#     blue_num += 1
#     return 1
#   else:
#     return 0


# length = int(sys.stdin.readline())
# squre = [list(map(int, sys.stdin.readline().split())) for _ in range(length)]

# white_num = 0
# blue_num = 0
# t_sum = 0
# for i in range(length):
#   t_sum += sum(squre[i])
# if color_check(squre, length) == 1: 
#   pass
# else:
#   paper_cut(squre, length//2)
# print(white_num)
# print(blue_num)

  
# import sys
# def paper_cut(x_start, y_start, length):
#   global white_num
#   global blue_num
#   half_length = length // 2
#   start_color = square[x_start][y_start]
#   for i in range(x_start, x_start + length):
#     for j in range(y_start, y_start + length):
#       if square[i][j] != start_color:
#         paper_cut(x_start, y_start, half_length)
#         paper_cut(x_start + half_length, y_start, half_length)
#         paper_cut(x_start, y_start + half_length, half_length)
#         paper_cut(x_start + half_length, y_start + half_length, half_length)
#         return


#   if start_color == 0:
#     white_num += 1
#   else: #start_color == 1
#     blue_num += 1


# length = int(sys.stdin.readline())
# square = [list(map(int, sys.stdin.readline().split())) for _ in range(length)]
# white_num = 0
# blue_num = 0
# paper_cut(0, 0 ,length)


# print(white_num)
# print(blue_num)

import sys
def paper_cut(x_start, y_start, length):
  global white_num
  global blue_num
  half_length = length // 2
  start_color = square[x_start][y_start]
  
  for i in range(x_start, x_start + length):
    print(f'sum: {sum(square[i][i:i+length])}')
    print(f'x_start, y_start, length: {x_start}, {y_start}, {length}')
    if (sum(square[i][y_start:y_start+length]) != length) and (sum(square[i][y_start:y_start+length]) != 0) :
      paper_cut(x_start, y_start, half_length)
      paper_cut(x_start + half_length, y_start, half_length)
      paper_cut(x_start, y_start + half_length, half_length)
      paper_cut(x_start + half_length, y_start + half_length, half_length)
      return


  if start_color == 0:
    white_num += 1
  else: #start_color == 1
    blue_num += 1


length = int(sys.stdin.readline())
square = [list(map(int, sys.stdin.readline().split())) for _ in range(length)]
white_num = 0
blue_num = 0
paper_cut(0, 0 ,length)


print(white_num)
print(blue_num)