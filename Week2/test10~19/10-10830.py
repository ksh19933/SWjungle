import sys

def matrix_multiplication(a, b, n):
  result = [ [0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        result[i][j] += a[i][k] * b[k][j]
      result[i][j] %= 1000
  return result
def matrix_divide(a, b, n):
  if b == 1:
    return a
  temp = matrix_divide(a, b//2, n)

  if b%2==0:
    return matrix_multiplication(temp, temp, n)
  else:
    return matrix_multiplication(matrix_multiplication(temp, temp, n), a, n)


n, b = map(int, sys.stdin.readline().split())

a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = matrix_divide(a, b, n)

for i in range(n):
  for j in range(n):
    print(result[i][j]%1000, end = " ")
  print()