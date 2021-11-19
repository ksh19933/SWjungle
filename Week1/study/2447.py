# def print_star(length, start_row, start_column):
#   if length >= 3:
#     for i in range(start_row + (length//3), start_row + 2 * (length//3)):
#       for j in range(start_column+ (length//3), start_column + 2 * (length//3)):
#         square[i][j] = ' '
#     for k in range(start_row, max_length, length//3):
#       for a in range(start_column, max_length, length//3):
#         print_star(length//3, k, a)

# max_length = int(input())
# square = [["*"]*max_length for _ in range(max_length)]
# print_star(max_length, 0, 0)
# for i in range(max_length):
#   for j in range(max_length):
#     print(square[i][j], end='')
#   print()
import sys
def draw_star(length):
  if length == 3:
    return ['***', '* *', '***']
  star = draw_star(length//3)
  board = []
  t = length // 3
  for i in range(t):
    board.append(star[i]*3)
  for j in range(t):
    board.append(star[j]+ ' '*(t) + star[j])
  for i in range(t):
    board.append(star[i]*3)
  return board

length = int(input())
result = draw_star(length)
for i in range(len(result)):
  print(result[i])

