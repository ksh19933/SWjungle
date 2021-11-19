num_case = int(input())
cases = []
for i in range(num_case):
  cases.append(input())
for case in cases:
  score, con = 0, 0
  for i in range(len(case)):
    if(case[i] == "O"):
      con += 1
      score += con
    else:
      con = 0
  print(score)
