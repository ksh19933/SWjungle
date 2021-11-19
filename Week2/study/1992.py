import sys

def quad_tree(x, y, length):
  if length == 1:
    return arr[x][y]
  
  start = arr[x][y]
  half = length // 2
  result = ""
  for i in range(x, x+length):
    for j in range(y, y+length):
      if arr[i][j] != start:
        result += quad_tree(x, y, half)
        result += quad_tree(x, y+half, half)
        result += quad_tree(x+half, y, half)
        result += quad_tree(x+half, y+half, half)
        if len(result) >= 4:
          result = "(" + result + ")" 
        return result     

  result += start
  if len(result) >= 4:
    result = "(" + result + ")"
  return result



n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline()) for _ in range(n)]

quad = quad_tree(0, 0, n)
print(quad)