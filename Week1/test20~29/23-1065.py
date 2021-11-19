# def seq_check(num):
#   if(num <1000):
#     d_n = []
#     while(num != 0):
#       d_n.append(num%10)
#       num = num//10
#     if d_n[0]-d_n[1] == d_n[1]-d_n[2]:
#       return 1
#     else:
#       return 0
#   else:
#     return 0

# num = int(input())
# if num < 100:
#   print(num)
# elif num <= 1000:
#   n_seq = 99
#   for i in range(100, num+1):
#     n_seq += seq_check(i)
#   print(n_seq)

def hasu_check(num):
  i_num = []
  for s_num in num:
    i_num.append(int(s_num))
  diff = i_num[0] - i_num[1]

  for i in range(1, len(i_num)-1):
    if (i_num[i] - i_num[i+1]) != diff:
      return 0
  return 1

n = int(input())
ctn = 99
if n < 100:
  print(n)
else:
  for i in range(100, n+1):
    ctn += hasu_check(str(i))
  print(ctn)





