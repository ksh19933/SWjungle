import sys

def binary_search(arr, pl, pr, key):
  while(True):
    pc = (pl+pr) //2
    if pl > pr:
      return 0
    if arr[pc] == key:
      return 1
    elif arr[pc] > key:
      pr = pc - 1
    elif arr[pc] < key:
      pl = pc + 1

n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
arr1.sort()
m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

for num in arr2:
  idx = binary_search(arr1, 0, n-1, num)
  print(idx)

