import sys
input = sys.stdin.readline

def put_operator(idx, cur_num, add, sub, mul, div):
  global max_num
  global min_num
  if idx == len(arr):
    if cur_num > max_num: max_num = cur_num
    if cur_num < min_num: min_num = cur_num
    return 
  # 더하기
  if add:
    put_operator(idx+1, cur_num+arr[idx], add-1, sub, mul, div)
  # 빼기
  if sub:
    put_operator(idx+1, cur_num-arr[idx], add, sub-1, mul, div)
  # 곱하기
  if mul:
    put_operator(idx+1, cur_num*arr[idx], add, sub, mul-1, div)
  # 나누기
  if div:
    put_operator(idx+1, int(cur_num /arr[idx]), add, sub, mul, div-1)

n = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_num = -sys.maxsize
min_num = sys.maxsize

put_operator(1, arr[0], operator[0], operator[1], operator[2], operator[3])

print(max_num)
print(min_num)