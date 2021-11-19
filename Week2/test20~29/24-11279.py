import sys
class MaxHeap:
  def __init__(self) -> None:
      self.data = [None]

  def insert(self, value):
    self.data.append(value)
    i = len(self.data) -1

    while i > 1:
      if self.data[i//2] < value:
        self.data[i//2], self.data[i] = self.data[i], self.data[i//2]
        i //= 2
      else:
        break
    
  def remove(self):
    if len(self.data) > 1:
      self.data[1], self.data[-1] = self.data[-1], self.data[1]
      data = self.data.pop()
      self.MaxHeapify(1)
    else:
      data = None
    return data

  def MaxHeapify(self, i):
    left = 2 * i
    right = 2 * i + 1
    max_index = i
    # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 값이 더 큰지를 판단
    if left < len(self.data) and self.data[left] > self.data[max_index]:
      max_index = left
    # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 값이 더 큰지를 판단
    if right < len(self.data) and self.data[right] > self.data[max_index]:
      max_index = right

    if max_index != i:
      self.data[i], self.data[max_index] = self.data[max_index], self.data[i]
      self.MaxHeapify(max_index)




n = int(sys.stdin.readline())

heap = MaxHeap()

for i in range(n):
  input_ = int(sys.stdin.readline())
  if input_ == 0:
    if len(heap.data) == 1:
      print(0)
    else:
      print(heap.remove())
  else:
    heap.insert(input_)