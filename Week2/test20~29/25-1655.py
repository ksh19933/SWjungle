import sys
import heapq
n = int(sys.stdin.readline())
maxHeap = []
minHeap = []
for i in range(n):
  num = int(sys.stdin.readline())
  if len(maxHeap) == len(minHeap):
    heapq.heappush(maxHeap, (-num, num))
  else:
    heapq.heappush(minHeap, (num, num))


  if minHeap and minHeap[0][1] < maxHeap[0][1]:
    min_pop = heapq.heappop(minHeap)[1]
    max_pop = heapq.heappop(maxHeap)[1]
    heapq.heappush(maxHeap, (-min_pop, min_pop))
    heapq.heappush(minHeap, (max_pop, max_pop))
  print(maxHeap[0][1])

