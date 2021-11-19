#7로 나누어서 요일 출력
def day_check(day):
  if day%7 == 1:
    print("MON")
  elif day%7 == 2:
    print("TUE")
  elif day%7 == 3:
    print("WED")
  elif day%7 == 4:
    print("THU")
  elif day%7 == 5:
    print("FRI")
  elif day%7 == 6:
    print("SAT")
  elif day%7 == 0:
    print("SUN")

target_month, target_day = map(int, input().split()) 

month = 1
day = target_day
day_31 = [1, 3, 5, 7, 8, 10, 12]
day_30 = [4, 6, 9, 11]

#위에 달에 맞추어 day를 더한다.
while (month != target_month):
  if month == 2:
    day += 28
  elif month in day_31:
    day += 31
  elif month in day_30:
    day += 30
  month += 1

day_check(day)


