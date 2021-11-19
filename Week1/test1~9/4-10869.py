score = int(input())
if score > 0:
  if score >= 90:
    print("A")
  elif score >= 80:
    print("B")
  elif score >= 70:
    print("C")
  elif score >= 60:
    print("D")
  else:
    print('F')
else:
  print("점수를 잘 못 입력했습니다. 확인해보세요.")
