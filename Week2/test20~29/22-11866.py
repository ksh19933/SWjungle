import sys


class Josephus_circle:
  def __init__(self, capacity) -> None:
      self.capacity = capacity
      self.que = [i for i in range(1, capacity +1)]
      self.front = 0
      self.rear = 0
      self.no = capacity

  def deque(self):
    value = self.que[self.front]
    self.front += 1
    self.no -= 1
    if self.front == self.capacity:
      self.front = 0
    return value
  
  def enque(self, value):
    self.que[self.rear] = value
    self.no += 1
    self.rear += 1
    if self.rear == self.capacity:
      self.rear = 0

people_num, move_ = map(int, sys.stdin.readline().split())
circle_ = Josephus_circle(people_num)

# for i in range(1, people_num+1):
#   circle_.enque(i)
result = []
for i in range(people_num):
  for _ in range(move_-1):
    circle_.enque(circle_.deque())
  result.append(circle_.deque())
  # print(circle_.que)

print('<',end='')
for i in range(people_num-1):
  print(result[i], end=', ')

print(f'{result[-1]}>')



# people_num, move_ = map(int, sys.stdin.readline().split())
# circle_ = [i for i in range(1, people_num+1)]
# result = []
# for i in range(people_num):
#   for _ in range(move_-1):
#     circle_.append(circle_.remove(circle_[0]))
#   result.append(circle_.remove(circle_[0]))
#   print(circle_)

# print('<',end='')
# for i in range(people_num-1):
#   print(result[i], end=', ')

# print(f'{result[-1]}>')
