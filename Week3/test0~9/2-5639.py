import sys
sys.setrecursionlimit(10**9)
def postorder(start, end):
  ## start == root
  if start > end:
    return
  div = end + 1
  for i in range(start+1, end+1):
    ##루트보다 큰 수
    if num_list[start] < num_list[i]:
      ##오른쪽 노드의 시작 idx
      div = i
      break

  #왼쪽 노드
  postorder(start+1, div-1)
  #오른쪽 노드
  postorder(div, end)
  print(num_list[start])



num_list = []
count = 0

while count <= 10000:
  try:
    num = int(input())
  except:
    break
  count += 1
  num_list.append(num)
postorder(0, len(num_list) - 1)


