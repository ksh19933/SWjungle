import sys
# 함수에는 시작 idx를 넣는다, arr[idx]를 더하고 다음 idx부터 추가한다.
def password_finder(chosen, idx):
  if len(chosen) == password_length:
    print(password_list)
    password_list.append(''.join(map(str,chosen)))
    return
  for i in range(idx, character_num):
    chosen.append(arr[i])
    password_finder(chosen, i+1)
    chosen.pop()
password_length, character_num = list(map(int, input().split()))
arr = list(input().split())
arr.sort()
password_list = []
password_finder([], 0)
#자음 모음 조건
for word in password_list:
  con = 0
  vow = 0
  for c in word:
    if c in 'aeiou':
      con += 1
    else:
      vow += 1
  #조건을 만족하면 출력
  if (con >= 1) and (vow >= 2):
    print(word)