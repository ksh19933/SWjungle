n, row, col = list(map(int,input().split()))
cnt = 0

while(n > 0):
  axis = 2**(n-1)
  #2사분면
  if (row < axis) & (col >= axis):
    cnt += axis**2
    col -= axis
  #3사분면
  elif (row >= axis) & (col < axis):
    cnt += (axis**2)*2
    row -= axis
  #4사분면
  elif (row >= axis) & (col >= axis):
    cnt += 3*(axis**2)
    row -= axis
    col -= axis
  n -= 1

if (row == 1)&(col == 0):
  cnt += 1
elif (col == 1)&(row == 0):
  cnt += 2
elif (col == 1)&(row == 1):
  cnt += 3
print(cnt)
      


