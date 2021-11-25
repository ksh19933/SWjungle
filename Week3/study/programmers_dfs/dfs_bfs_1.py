def dfs(numbers, idx, sum, target):
  cnt = 0
  if idx == len(numbers):
    if sum == target:
      return 1
    return 0
  
  cnt += dfs(idx+1, sum+numbers[idx], target)
  cnt += dfs(idx+1, sum-numbers[idx], target)

  return cnt

def solution(numbers, target):
    answer = 0
    answer = dfs(numbers, 0, 0, target)
    return answer