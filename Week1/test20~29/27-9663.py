# def put() -> None:
#   #각 열에 배치한 퀸의 위치를 출력
#   for i in range(n):
#     print(f'{pos[i]:2}', end = '')
#   print()
# n = int(input())

# def n_queen(qn,n):
#   global count
#   #row check
#   if qn == n:
#     count += 1
#     return
#   else:
#     for j in range(n):
#       if (not flag_h[j] and not flag_b[qn+j] and not flag_c[qn-j+n-1]):
#         flag_h[j] = flag_b[qn+j] = flag_c[qn-j+n-1] = True 
#         n_queen(qn+1,n)
#         flag_h[j] = flag_b[qn+j] = flag_c[qn-j+n-1] = False


def put() -> None:
  #각 열에 배치한 퀸의 위치를 출력
  for i in range(n):
    print(f'{pos[i]:2}', end = '')
  print()

def n_queen(queen_located, n):
  global count
  if queen_located == n:
    put()
    count += 1 
    return
  else:
    for j in range(n):
      if not flag_h[j] and not flag_b[queen_located+j] and not flag_c[queen_located-j+(n-1)]:
        pos[queen_located] = j
        flag_h[j] = flag_b[queen_located+j] = flag_c[queen_located-j+(n-1)] = True
        n_queen(queen_located+1, n)
        flag_h[j] = flag_b[queen_located+j] = flag_c[queen_located-j+(n-1)] = False
        pos[queen_located] = 0



n = 4
count = 0
pos= [0] * 4
flag_h = [False]*n # 각 row에 퀸이 배치되어 있는지 체크
flag_b = [False]*(2*n-1)
flag_c = [False]*(2*n-1)
##n_queen(퀸이 놓여질 행의 위치, 체스판 크기)
n_queen(0, n)
print(count)










