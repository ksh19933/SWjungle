import sys

cen_word = list(sys.stdin.readline().strip())
reversed_word = cen_word[::-1]
leng = len(cen_word)
arr = sys.stdin.readline().strip()

front_idx = 0
back_idx = len(arr) - 1
front = []
back = []
is_left = True
while front_idx <= back_idx:
  if is_left:
    front.append(arr[front_idx])
    front_idx += 1
    if front[-leng:] == cen_word:
      front[-leng:] = []
      is_left = False
  else:
    back.append(arr[back_idx])
    back_idx -= 1
    if back[-leng:] == reversed_word:
      back[-leng:] = []
      is_left = True
for i in range(len(back)):
  front.append(back.pop())
  if front[-leng:] == cen_word:
    front[-leng:] = []

print(''.join(front))