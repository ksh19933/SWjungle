import sys
import math
# N = int(input())
# # num만큼의 수를 담을 수 있는 리스트 a_list 생성
# a = [True] * 10001
# # 2부터 num의 사이의 수 중에 소수가 있는지 확인하고 소수이면 그의 배수들을 False로 바꾼다.
# for i in range(2, len(a)):
#   if a[i] == True:
#     for j in range(i+i, len(a), i):
#       a[j] = False

# for i in range(N):
#   num = int(input())
#   # 약수의 합이 주어진 수가 되는 약수들을 찾고 그 수의 차이가 최소일 경우를 min 리스트에 넣는다.
#   for i in range(int(num/2), num, 1):
#     if a[i] & a[num-i]:
#       print(num-i, i)
#       break

N = int(sys.stdin.readline())

# 1~ 10000까지의 수들이 담긴 True 배열을 만들고 소수가 아닌 수를 False로 바꿔준다.
a = [True] * 10001
for i in range(2, 10001):
  if a[i] == True:
    for j in range(2*i, 10001, i):
      a[j] = False

num_list = [int(sys.stdin.readline()) for _ in range(N)]

for num in num_list:
  for i in range(num//2+1):
    left = num//2 - i
    right = num//2 + i
    if a[left] and a[right]:
      print(left, right)
      break



