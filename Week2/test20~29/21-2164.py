import sys
n = int(sys.stdin.readline())
q = []
ptr = 0
for i in range(1,n+1):
  q.append(i)
temp = 0
for _ in range(n-1):
  #pop
  ptr += 1
  #교체
  q.append(q[ptr])
  ptr += 1

print(q[ptr])
