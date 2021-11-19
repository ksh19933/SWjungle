import sys
class Stack():
  def __init__(self, capacity) -> None:
    self.capacity = capacity
    self.stk = [None] * capacity
    self.ptr = 0
    self.sum = 0

  def push(self, value):
    self.stk[self.ptr] = value
    self.sum += value
    self.ptr += 1

  def pop(self):
    if self.ptr == 0:
      return
    else:
      self.ptr -= 1
      self.sum -= self.stk[self.ptr]



#0일 때 pop,, 나머지는 push
n = int(sys.stdin.readline())
s = Stack(100000)
for i in range(n):
  num = int(sys.stdin.readline())
  if num == 0:
    s.pop()
  else:
    s.push(num)

print(s.sum)