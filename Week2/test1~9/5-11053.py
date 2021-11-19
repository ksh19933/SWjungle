import sys
def lower_bound(pl, pr, num):
  while pl < pr:
    pc = (pl + pr) //2
    if num > dynamic_arr[pc]:
      pl = pc + 1
    else: # num <= dynamic_arr[pc]:
      pr = pc
  return pl


#시작
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dynamic_arr = [arr[0]]
for i in range(1, n):
  if dynamic_arr[-1] < arr[i]:
    dynamic_arr.append(arr[i])
  else: #dynamic_arr의 마지막 원소보다 arr[i]가 작을 때
    idx = lower_bound(0, len(dynamic_arr) - 1, arr[i])
    dynamic_arr[idx] = arr[i]

print(len(dynamic_arr))