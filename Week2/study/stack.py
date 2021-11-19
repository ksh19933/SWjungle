from typing import Any
class FixedStrack:

  class Empty(Exception):
    #비어 있는 FixedStack에 팝 또는 피크할 때 내보내는 예외처리
    pass

  class Full(Exception):
    pass

  def __init__(self, capacity: int = 256) -> None:
    self.stk = [None] * capacity
    self.capacity = capacity
    self.ptr = 0

  
  def __len__(self) -> int:
    #스택에 쌓여 있는 데이터 개수를 반환
    return self.ptr


  def is_empty(self) -> bool:
    #스택이 비어있는지 확인
    return self.ptr <= 0

  def is_full(self) -> bool:
    #스택이 가득 차 있는지 판단
    return self.ptr >= self.capacity


  def push(self, value):
    if self.is_full:
      raise FixedStrack.Full
    self.stk[self.ptr] = value
    self.ptr += 1

  def pop(self):
    if self.is_empty:
      raise FixedStrack.is_empty
    self.ptr -= 1
    return self.stk[self.ptr]

  def peek(self):
    if self.is_empty():
      raise FixedStrack.Empty
    return self.stk[self.ptr-1]

  def clear(self):
    self.ptr = 0
  
  def find(self, value):
    for i in range(self.ptr-1, -1, -1):
      if self.stk[i] == value:
        return i
    return -1
  
  def count(self, value):
    ctn = 0
    for i in range(self.ptr):
      if self.stk[i] == value:
        ctn +=1
    return ctn
  
  def __contains__(self, value):
    return self.count(value) > 0

  def dump(self, value):
    if self.is_empty():
      print('스택이 비어있습니다.')
    else:
      print(self.stk[:self.ptr])

s = FixedStrack(64)



