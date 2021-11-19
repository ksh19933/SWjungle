import sys
def router(arr, pl, pr, router_num):
  result = 0
  while pl <= pr:
    pc = (pl+pr) // 2
    current_location = arr[0]
    used = 1
    for i in range(1, len(arr)):
      if arr[i] >= pc + current_location:
        used += 1
        current_location = arr[i]
    if used >= router_num:
      result = pc
      pl = pc + 1
    else:
      pr = pc - 1

  print(result)

n, c = map(int, input().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()
router(arr, 1, arr[-1] - arr[0], c)