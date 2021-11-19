import sys

def cnn(x, y, length):
  if length == 2:
    temp = []
    for i in range(x, x+length):
      for j in range(y, y+length):
        temp.append(arr[i][j])
    temp.sort()
    return temp[-2]
  half = length // 2
  temp = [cnn(x, y , half),
          cnn(x+half, y, half),
          cnn(x, y+half, half),
          cnn(x+half, y+half, half)
  ]
  temp.sort()
  return temp[-2]


n = int(sys.stdin.readline())
arr= [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(cnn(0,0,n))
