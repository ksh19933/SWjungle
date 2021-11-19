a = [4,7,3,2,5]
n = len(a)
for i in range(1,n):
  print(a)
  key = a[i]
  pl = 0 #검색 범위의 맨 앞 원속 인덱스
  pr = i-1 #검색 범위의 맨 끝 원소 인덱스
  while True:
    pc = (pl + pr) // 2
    print(f'key: {key}')
    print(f'pl, pr, pc: {pl, pr, pc}')
    if a[pc] == key:
      print(a[pc])
      break
    elif a[pc] < key:
      pl = pc + 1
      print("out1")
    elif a[pc] > key:
      pr = pc - 1
      print("out2")
    if pl > pr:
      break
  print(f'pl, pr, pc: {pl, pr, pc}')
  
  pd = pc + 1 if pl <= pr else pr + 1 #삽입해야 할 위치의 인덱스
  print(f'pd: {pd}')
  for j in range(i, pd, -1):
    print('change')
    a[j] = a[j-1]
  a[pd] = key
  print(a)

print(a)