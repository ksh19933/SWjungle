year = int(input())
leap_year = 0
if((year%4 ==0) & (year%100 != 0)) or(year%400 == 0):
  leap_year = 1

print(leap_year)