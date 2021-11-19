from __future__ import annotations
from typing import Any, Type

class Node:
  #이진 검색 트리의 노드
  def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
  ##생성자
    self.key = key #키
    self.value = value #값 
    self.left = left #왼쪽 포인터
    self.right = right #오른쪽 포인터

class BinarySearchTree:
  #이진 검색 트리
  def __init__(self):
    #초기화
    self.root = None

def search(self, key):
  #키가 key인 노드를 검색
  p = self.root
  while True:
    if p is None:
      return None
    if key == p.key:
      return p.value
    elif key < p.key:
      p = p.left
    else:
      p = p.right

def add(self, key, value):
  def add_node(node, key, value):
    if key == node.key:
      print("이미 같은 키 값을 가지는 노드가 존재합니다")
      return False
    elif key < node.key:
      if node.left is None:
        node.left = Node(key, value, None, None)
      else:
        add_node(node.left, key, value)
    else: #key > node.key
      if node.right == None:
        node.right = Node(key, value, None, None)
      else:
        add_node(node.right, key, value)
      return True
  if self.root is None:
    self.root = Node(key, value, None, None)
    return True
  else:
    return add_node(self.root, key, value)

print("hi")
