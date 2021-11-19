import sys
import heapq


n = int(sys.stdin.readline())
que = []
for _ in range(n):
  num = int(sys.stdin.readline())
  heapq.heappush(que, num)

sum = 0
for i in range(n):
  if len(que) > 1:
    temp_num1 = heapq.heappop(que)
    temp_num2 = heapq.heappop(que)
    heapq.heappush(que, temp_num1+temp_num2)
    sum += temp_num1 + temp_num2


print(sum)
