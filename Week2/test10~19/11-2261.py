import sys
#나눈 후에 결과를 반환해주는 함수 정의
def divide_axis(left, right):
  if left == right:
    return sys.maxsize
  mid = (left + right) // 2
  res = min(divide_axis(left, mid), divide_axis(mid+1,right))
  less_length_dots = []
  #중앙점부터 x축을 기준으로 왼쪽으로 가면서 length이하의 점들을 찾고 less_length_dots에 넣는다
  for mid_to_left in range(mid, left-1, -1):
    if (dots[mid_to_left][0] - dots[mid][0])**2 < res: 
      less_length_dots.append(dots[mid_to_left])
    else:
      break
  #중앙점부터 x축을 기준으로 오른쪽으로 가면서 length이하의 점들을 찾고 less_length_dots에 넣는다
  for mid_to_right in range(mid+1, right+1):
    if (dots[mid_to_right][0] - dots[mid][0])**2 < res:
      less_length_dots.append(dots[mid_to_right])
    else:
      break
  #저장한 점들을 0번부터 시작하여 하나씩 비교 // 이때 res보다 클 경우 break
  less_length_dots.sort(key= lambda x: x[1])
  for i in range(len(less_length_dots) -1):
    for j in range(i +1, len(less_length_dots)):
      if (less_length_dots[i][1] - less_length_dots[j][1])**2 < res:
        res = min(res, length_calculate(less_length_dots[i], less_length_dots[j]))
      else:
        break

  return res
  

def length_calculate(dot1, dot2):
  return (dot2[0] - dot1[0])**2 + (dot2[1] - dot1[1])**2




n = int(sys.stdin.readline())
dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
dots.sort()
if len(dots) != len(set(dots)):
  print("0")
else:
  print(divide_axis(0, n-1))
