case_num = int(input())
for i in range(case_num):
  N, STR = input().split(" ")
  P = ""
  for str in STR:
    P += str*int(N)
  print(P)