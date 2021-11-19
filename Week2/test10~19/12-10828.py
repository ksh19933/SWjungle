import sys
class Stack:
  def __init__(self, capacity) -> None:
      self.capacity = capacity
      self.stk = [None] * capacity
      self.ptr = 0

  def push(self, value):
    self.stk[self.ptr] = value
    self.ptr += 1
  
  def pop(self):
    if self.empty():
      return -1
    else:
      self.ptr -= 1
      return self.stk[self.ptr]
  
  def size(self):
    return self.ptr

  def empty(self):
    if self.ptr == 0:
      return 1
    else:
      return 0

  def top(self):
    if self.empty():
      return -1
    else:
      return self.stk[self.ptr - 1]

n = int(sys.stdin.readline())


s = Stack(10000)

for i in range(n):
  order = list(sys.stdin.readline().split())
  if order[0] == "push":
    s.push(int(order[1]))
  elif order[0] == "top":
    print(s.top())
  elif order[0] == "size":
    print(s.size())
  elif order[0] == 'empty':
    print(s.empty())
  elif order[0] == 'pop':
    print(s.pop())

