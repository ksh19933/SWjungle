import sys
n = int(sys.stdin.readline())

for i in range(n):
  ps = sys.stdin.readline().strip()
  s = []
  flag = 0
  for p in ps:
    if (len(s) == 0) & (p != "("):
      flag = 0
      print("NO")
      break
    elif p == "(":
      flag = 1
      s.append(1)
    else:
      s.pop()

  if flag == 1:
    if len(s) == 0:
      print("YES")
    else:
      print("NO")

