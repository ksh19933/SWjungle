import sys

num_case = int(input())
cases =[int(sys.stdin.readline()) for _ in range(num_case)]

for case in cases:
  total = 0
  stu = 0
  for i in range(1, case[0]+1):
    total += case[i]
  avg = total/case[0]
  for i in range(1, case[0]+1):
    if case[i] > avg:
      stu += 1
  print(f'{stu*100/case[0]:.3f}%')
