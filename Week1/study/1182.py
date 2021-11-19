import sys
def parital_sequence(arr, idx, sum, target_sum):
  global ctn
  if len(arr) <= idx:
    return
  #하나를 더함
  sum += arr[idx]
  if sum == target_sum:
    ctn += 1
  #arr[idx]를 빼고 다음  arr[idx]를 더하는 함수 호출
  parital_sequence(arr, idx+1, sum-arr[idx], target_sum)
  #arr[idx]를 나두고 다음 arr[idx]를 더하는 함수 호출
  parital_sequence(arr, idx+1, sum, target_sum)

ctn = 0
n, target_sum = list(map(int, input().split()))
arr = list(map(int, input().split()))
parital_sequence(arr, 0, 0, target_sum)
print(ctn)