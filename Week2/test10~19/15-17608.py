import sys

n = int(sys.stdin.readline())
s = [int(sys.stdin.readline()) for _ in range(n)]
key = s[-1]
ctn = 1
for i in range(n-2, -1, -1):
  if s[i] > key:
    key = s[i]
    ctn += 1

print(ctn)