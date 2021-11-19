import sys

num = int(sys.stdin.readline().strip())
height_arr  = [int(sys.stdin.readline().strip()) for _ in range(num)]

stack = []
min_height = 0
max_area = 0
for i in range(num):
  # 스택에는 원소의 idx를 저장
  # 스택의 원소[-1]과 height_arr[i]를 비교하여 height 원소의 높이가 낮을 경우에 빼면서 넓이를 구한다.
  # 이때 빠진  height * 너비(i - stack[-1])를 해준다.
  while stack and height_arr[stack[-1]] > height_arr[i]:
    temp = stack.pop()
    if len(stack) == 0:
      width = i
    else:
      width = i - stack[-1] - 1
    max_area = max(max_area, height_arr[temp] * width)
  # 스택에 원소를 추가
  stack.append(i)

while stack:
    temp = stack.pop()
    if len(stack) == 0:
      width = num
    else:
      width = num - stack[-1] - 1
    max_area = max(max_area, height_arr[temp] * width)

print(max_area)