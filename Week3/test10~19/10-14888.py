import sys

input = sys.stdin.readline
##idx는 1부터 시작  result = arr[0]부터 시작
def put_operator(idx, result):
  global max_num
  global min_num
  if idx == len(arr):
    #max, min check
    if result > max_num:
      max_num = result
    if result < min_num:
      min_num = result
    return 
  
  for i in range(4):
    if i == 0 and operator[i] != 0:
      #더하기
      operator[i] -= 1
      result = result + arr[idx]
      put_operator(idx+1, result)
      operator[i] += 1
      result = result - arr[idx]
      #빼기
    elif i == 1 and operator[i] != 0:
      operator[i] -= 1
      result = result - arr[idx]
      put_operator(idx+1, result)
      operator[i] += 1
      result = result + arr[idx]
      #곱하기
    elif i == 2 and operator[i] != 0:
      operator[i] -= 1
      result = result * arr[idx]
      put_operator(idx+1, result)
      operator[i] += 1
      result = result // arr[idx]
      #나누기
    elif i == 3 and operator[i] != 0:
      operator[i] -= 1
      temp = result
      #음수 일 때
      if result < 0 and arr[idx] > 0:
        result = -((-result) // arr[idx])
      #양수 일 때
      else:
        result = result // arr[idx]
      put_operator(idx+1, result)
      result = temp
      operator[i] += 1

n = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_num = -sys.maxsize
min_num = sys.maxsize

put_operator(1, arr[0])

print(max_num)
print(min_num)