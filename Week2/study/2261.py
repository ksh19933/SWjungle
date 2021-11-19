import sys
def length_calculate(p1, p2):
  return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

# 재귀함수
def divide_star(left, right):
  if left == right:
    return sys.maxsize
  #mid 구하기
  mid = (left + right) // 2
  #mid를 기준으로 분할후 분할 지역의 최소 거리를 재귀적으로 받는다.
  min_length = min(divide_star(left, mid), divide_star(mid+1, right))
  #mid와 가장 가까운 점을 기준으로 해서 x축이 최소거리 안에 있는 점을 찾는다.
  mtl = mid
  mtr = mid + 1
  less_stars = []
  #왼쪽으로 이동하면서 점을 구함
  while(left <= mtl):
    if(arr[mid][0] - arr[mtl][0])**2 < min_length:
      less_stars.append(arr[mtl])
    mtl -= 1
  #오른쪽으로 이동하면서 점을 구함
  while(mtr <= right):
    if (arr[mid][0] - arr[mtr][0])**2 < min_length:
      less_stars.append(arr[mtr])
    mtr += 1

  #위에서 구한 점들의 집합을 y축을 기준으로 정렬
  less_stars.sort(key = lambda x: x[1])
  #0번 점부터 시작하여 최소거리 안에 속해 있는 점들과 거리를 측정
  for i in range(len(less_stars)):
    for j in range(i+1, len(less_stars)):
      if (less_stars[i][1] - less_stars[j][1])**2 >= min_length:
        break
      else:
        min_length = min(min_length, length_calculate(less_stars[i], less_stars[j]))

  return min_length

n = int(sys.stdin.readline())
arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr.sort()
if len(arr) != len(set(arr)):
  print("0")
else:
  print(divide_star(0, n-1))
