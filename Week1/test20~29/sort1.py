a = [9, 1, 3, 4, 6, 7, 8]
n = len(a)
k = 0
cnt = 0
snt = 0
while k < n - 1:
  last = n - 1
  for j in range(n-1, k, -1):
    cnt += 1
    if a[j] < a[j-1]:
      snt += 1
      a[j] , a[j-1] = a[j-1], a[j]
      last = j
  k = last
  print(a)

print(f'비교를 {cnt}번 진행했습니다.')
print(f'교환을 {snt}번 진행했습니다.')