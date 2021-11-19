import sys
num = int(input())
n_list = [int(sys.stdin.readline()) for i in range(num)]
k = 0
while k < num - 1:
  last = num - 1
  for j in range(num-1, k, -1):
    if n_list[j] < n_list[j-1]:
      n_list[j] , n_list[j-1] = n_list[j-1], n_list[j]
      last = j
  k = last
for n in n_list:
  print(n)

