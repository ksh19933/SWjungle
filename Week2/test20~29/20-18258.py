import sys
class Queue:
  def __init__(self, capacity):
    self.capacity = capacity
    self.que = [None] * capacity
    self.front_ = 0
    self.rear = 0
    self.no = 0

  def push(self, value):
    self.que[self.rear] = value
    self.no += 1
    self.rear += 1
    if self.rear == self.capacity:
      self.rear = 0
  
  def pop(self):
    if self.no == 0:
      return -1
    value = self.que[self.front_]
    self.no -= 1
    self.front_ += 1
    if self.front_ == self.capacity:
      self.front_ = 0
    return value
  def size(self):
    return self.no

  def empty(self):
    if self.no <= 0:
      return 1
    else:
      return 0
  
  def front(self):
    if self.no == 0:
      return -1
    return self.que[self.front_]

  def back(self):
    if self.no == 0:
      return -1
    return self.que[self.rear-1]


n = int(sys.stdin.readline())
q = Queue(2000000)

for _ in range(n):
  order = list(sys.stdin.readline().split())

  if order[0] == "push":
    q.push(int(order[1]))
  elif order[0] == "front":
    print(q.front())
  elif order[0] == "back":
    print(q.back())  
  elif order[0] == "size":
    print(q.size())
  elif order[0] == 'empty':
    print(q.empty())
  elif order[0] == 'pop':
    print(q.pop())


import sys

n = int(sys.stdin.readline())
q = []
ptr = 0
for _ in range(n):
  order = list(sys.stdin.readline().split())
  if order[0] == "push":
    q.append(int(order[1]))
  elif order[0] == 'pop':
    if len(q) > ptr:
      print(q[ptr])
      ptr += 1
    else:
      print(-1)
  elif order[0] == "size":
    print(len(q)-ptr)
  elif order[0] == 'empty':
    if len(q) == ptr:
      print(1)
      ptr = 0
      q = []
    else:
      print(0)
  elif order[0] == "front":
    if len(q) > ptr: print(q[ptr])
    else: print(-1)
  elif order[0] == "back":
    if len(q) > ptr: print(q[-1]) 
    else: print(-1) 


