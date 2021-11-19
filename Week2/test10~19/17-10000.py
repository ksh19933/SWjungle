import sys

square_num = int(sys.stdin.readline().strip())
points = []
for i in range(square_num):
  x, r = map(int, sys.stdin.readline().split())
  points.append([x-r, 1])
  points.append([x+r, -1])

points.sort()
stack = []
area = 1
##하나씩 스택에 넣기
for point in points:
  #왼쪽 점일 경우
  # print(f'point: {point}')
  if point[1] == 1:
    stack.append(point)
    continue
  temp_length = 0
  #오른쪽 점일 경우
  while stack:
    print(stack)
    prev_stack = stack.pop()
    #prev_stack이 circle이 있을 경우 해당 원의 너비를 축적
    if prev_stack[1] == 0:
      temp_length += prev_stack[0]
    # stack을 pop 했을 때 왼쪽 점일 경우 합쳐서 원 좌표를 만든다
    elif prev_stack[1] == 1:
      width = point[0] - prev_stack[0]
      print(point[0], prev_stack[0])
      if temp_length == width:
        area += 2
      else:
        area += 1
      stack.append([width ,0])
      break
    # print(f'temp_length: {temp_length}')
    # print(f'area: {area}')

print(area)