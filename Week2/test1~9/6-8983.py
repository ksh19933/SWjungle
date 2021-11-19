# import sys
# #lower_bound def
# def lower_bound(pl, pr, num):
#   while pl < pr:
#     pc = (pl + pr) // 2
#     if num > bend_location[pc]:
#       pl = pc +1
#     else:
#       pr = pc
#   return pl
# #입력 받기
# bend_num, animal_num, range_ = map(int,sys.stdin.readline().split())
# bend_location = list(map(int, sys.stdin.readline().split()))
# animal_coordinates =[list(map(int, sys.stdin.readline().split())) for _ in range(animal_num)]
# bend_location.sort()
# ctn = 0
# #for문 돌면서 거리계산
# for animal_coordinate in animal_coordinates:
#   #lower_bound 함수를 이용해 동물과 가장 가까운 사대의 위치를 구한다.
#   idx = lower_bound(0, bend_num-1, animal_coordinate[0])
#   #구한 위치의 사대와 동물의 거리를 구한다.
#   length_ = abs(bend_location[idx] - animal_coordinate[0]) + animal_coordinate[1]
#   if length_ <= range_:
#     ctn += 1
  
# print(ctn)

import sys
#입력 받기
bend_num, animal_num, range_ = map(int,sys.stdin.readline().split())
bend_location = list(map(int, sys.stdin.readline().split()))
animal_coordinates =[list(map(int, sys.stdin.readline().split())) for _ in range(animal_num)]
bend_location.sort()
ctn = 0
#for문 돌면서 거리계산
for x_coordinate, y_coordinate in animal_coordinates:
  #lower_bound 함수를 이용해 동물과 가장 가까운 사대의 위치를 구한다.
  pl, pr = 0, bend_num-1
  while pl < pr:
    pc = (pl + pr) // 2
    if x_coordinate > bend_location[pc]:
      pl = pc +1
    else:
      pr = pc
  #구한 위치의 사대와 동물의 거리를 구한다.
  if (abs(bend_location[pl] - x_coordinate) + y_coordinate <= range_) or (abs(bend_location[pl - 1] - x_coordinate) + y_coordinate <= range_):
    ctn += 1
  
print(ctn)