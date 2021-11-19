import sys

strin = list(sys.stdin.readline().strip())
censor_word = list(sys.stdin.readline().strip())
len_word = len(censor_word)
front_idx = 0
end = len(strin)-1
front = []
flag = False
while not flag:
  while(front_idx <= end):
    flag = True
    front.append(strin[front_idx])
    front_idx += 1
    if front[-len_word:] == censor_word:
      front[-len_word:] = []
      flag = False
  strin = front.copy()
  if strin == []:
    break
  front = []
  front_idx = 0
  end = len(strin)-1

if strin == []:
  print("FRULA")
else:
  print(''.join(strin))