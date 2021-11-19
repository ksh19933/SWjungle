import sys
n = int(sys.stdin.readline())
k_num = int(sys.stdin.readline())

start = 1
end = n*n

while (start <= end):
  mid = (start + end) // 2
  cnt = 0
  for i in range(1, n+1):
    cnt += min(mid//i, n)
  if k_num <= cnt:
    end = mid - 1
  else:
    start = mid + 1
  print(start, mid)



print(start)





# arr = [0] * (k_num+1)
# for i in range(1, n+1):
#   for j in range(1, n+1):
#     key = i*j
#     if key < k_num:
#       arr[key] += 1
#       sum += arr[key]
#       ans = key
#       if sum > k_num:
#         break      
#   if k_num < i:
#     break