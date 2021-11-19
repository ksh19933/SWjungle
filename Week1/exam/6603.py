import sys
def lotto_pick(chosen,idx):
  if len(chosen) == 6:
    for i in range(len(chosen)):
      print(chosen[i], end=' ')
    print()
    return

  for i in range(idx, 50):
    if i in picks:
      chosen.append(i)
      lotto_pick(chosen, i+1)
      chosen.pop()

pick_num = 1

while pick_num != 0:
  testcase = list(map(int, sys.stdin.readline().split()))
  pick_num = testcase[0]
  picks = testcase[1:]
  lotto_pick([], 1)
  print()


###개선 시도
import sys
def lotto_pick(chosen):
  if len(chosen) == 6:
    for i in range(len(chosen)):
      print(chosen[i], end=' ')
    print()
    return

  for pick in picks:
    if pick not in chosen:
      chosen.append(pick)
      picks.remove(pick)
      lotto_pick(chosen)
      chosen.pop()

pick_num = 1
while pick_num != 0:
  testcase = list(map(int, sys.stdin.readline().split()))
  pick_num = testcase[0]
  picks = testcase[1:]
  lotto_pick([])
  print()