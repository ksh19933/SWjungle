def hanoi(n, one, two, three):
  if n > 1:
    hanoi(n-1, one, three, two)
  print(one, three)
  if n > 1:
    hanoi(n-1, two, one, three)


n = 3
hanoi(n, 1, 2, 3)