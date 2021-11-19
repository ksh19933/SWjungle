a = [9, 1, 3, 4, 6, 7, 8]
#양쪽에서 비교하며 정렬

cnt = 0
snt = 0

left = 0
right = len(a) - 1
last = right
while left < right:
  for i in range(right, left, -1):
    exchange = 0
    cnt+=1
    if a[i] < a[i-1]:
      a[i], a[i-1] = a[i-1], a[i]
      last = i
      snt+=1
      exchange += 1
    print(a)
  left = last

  for i in range(left, right):
    exchange = 0
    cnt+=1
    if a[i] > a[i+1]:
      a[i], a[i+1] = a[i+1], a[i]
      last = i
      snt+=1
      exchange += 1
    print(a)
  right = last
  print(exchange)


print(f'비교를 {cnt}번 진행했습니다.')
print(f'교환을 {snt}번 진행했습니다.')