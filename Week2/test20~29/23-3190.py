import sys
from collections import deque
### 보드를 생성하고 0을 입력
N = int(sys.stdin.readline().strip())
board = [[0] * N for _ in range(N)]

### 사과가 있는 곳을 1로 변경
apple_num = int(sys.stdin.readline().strip())
for _ in range(apple_num):
  i, j = map(int, sys.stdin.readline().split())
  board[i-1][j-1] = 1
### 방향 바뀜 정보
sec_num = int(sys.stdin.readline().strip())
direction_change_sec = [list(sys.stdin.readline().split()) for _ in range(sec_num)]
sec_flag = 0

### 그 좌표를 뱀의 que에 넣는다, 사과가 없을 경우 front에 있는 좌표를 que에서 뺀 후 0으로 변경
### 뱀의 이동 경로를 move로 표현
snake = deque()
snake.append([0,0])
head = [0,0]
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
direction = 0
sec = 0

while True:
  sec += 1
  print(f'sec: {sec}')
  print(snake)
  # 뱀 이동
  for i in range(2):
    head[i] += move[direction][i]
  print(head[0], head[1])
  if head[0] < 0 or head[1] < 0 or head[0] >= N or head[1] >= N:
    break
  else:
    # 뱀의 몸이 있을 경우, 즉 -1일 경우 break 
    if board[head[0]][head[1]] == -1:
      break
    # 사과가 있을 경우 snake에 좌표 정보를 그대로 넣는다  --> 1일 경우
    elif board[head[0]][head[1]] == 1:
      snake.append([head[0], head[1]])
      board[head[0]][head[1]] = -1
    # 사과가 없을 경우 snake의 front 정보를 빼고 그 좌표를 0으로 바꾼다
    else:
      snake.append([head[0], head[1]])
      tail_position = snake.popleft()
      board[tail_position[0]][tail_position[1]] = 0
      board[head[0]][head[1]] = -1



  ## 방향 전환
  if sec_flag < sec_num:
    # print(f'flag, num: {sec_flag}, {sec_num}')
    # print(f'방향 전환 정보: {direction_change_sec[sec_flag][0]}, {direction_change_sec[sec_flag][1]}')
    # print(f'sec : {sec}')
    if int(direction_change_sec[sec_flag][0]) == sec:
      # print('방향전환 시작')
      if direction_change_sec[sec_flag][1] == "D":
        direction += 1
        direction %= 4
      else:
        direction -= 1
        direction %= 4
      sec_flag += 1
      print(f'direction: {direction}')


print(sec)


