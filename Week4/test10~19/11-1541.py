import sys
input = sys.stdin.readline
nums = list(map(str, input().strip().split('-')))
for i in range(len(nums)):
    nums[i]= sum(list(map(int, nums[i].split('+'))))
result = nums[0]
for i in range(1, len(nums)):
    result -= nums[i]
print(result)