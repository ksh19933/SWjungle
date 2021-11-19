import sys
n = int(input())
room_list = [int(sys.stdin.readline()) for _ in range(n)]

for room_num in room_list:
  room_door = [False] * (room_num)
  for i in range(room_num):
    for j in range(i, room_num, i+1):
      if room_door[j]:
        room_door[j] = False
      else:
        room_door[j] = True
  ctn = 0
  for k in range(room_num):
    if room_door[k]:
      ctn += 1
  print(ctn)