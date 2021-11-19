# import sys
# n = int(sys.stdin.readline())
# arr = "moo"
# for i in range(1, n):
#   if(len(arr)+1 >= n):
#     print("m")
#     break
#   elif len(arr) + i+3 >= n:
#     print("o")
#     break
#   elif(2*len(arr) + i+3 >= n):
#     print(arr[n-(i+3+len(arr))])
#     break
#   arr = arr + "m" + "o"*(i+2)+ arr

# print(arr)

num = int(input())

k = 0
leng = 3
while leng < num:
  k = k + 1
  leng = 2 * leng + 3 + k

def dac(k, leng, num):
  if k == 0:
    if num == 1:
      return 'm'
    else:
      return 'o'
  leng = (leng - k - 3) //2
  k = k - 1
  if num <= leng:
    return dac(k, leng, num)
  elif num == leng+1:
    return 'm'
  elif num > leng + k +4:
    return dac(k, leng, num - leng - k -4)
  else:
    return 'o'

print(dac(k, leng, num))