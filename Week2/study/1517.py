import sys
sys.setrecursionlimit(10 ** 9)

def merge_sort(start, end):
  global swap, n_list
  size = end - start
  mid = (start + end) // 2
  #list를 divide 하고 정렬하는 재귀함수
  if size <= 1:
    return

  merge_sort(start, mid)
  merge_sort(mid, end)

  #병합
  temp = []
  idx1 , idx2= start, mid
  cnt = 0
  while idx1 < mid and idx2 < end:
    if n_list[idx1] > n_list[idx2]:
      temp.append(n_list[idx2])
      idx2 += 1
      cnt += 1
    else:
      temp.append(n_list[idx1])
      idx1 += 1
      swap += cnt

  while idx1 < mid:
    temp.append(n_list[idx1])
    idx1 += 1
    swap += cnt
    

  for k in range(len(temp)):
    n_list[start+k] = temp[k]

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
print(n_list)
swap = 0
merge_sort(0, n)
print(n_list)
print(swap)

