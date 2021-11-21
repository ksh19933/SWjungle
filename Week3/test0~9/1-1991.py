import sys

class Node:
  def __init__(self, value, left = None, right = None) -> None:
    self.value = value
    self.left = left
    self.right = right
##전위 순회
def preorder(node):
  print(node.value, end='')
  if node.left != '.':
    preorder(tree[node.left])
  if node.right != '.':
    preorder(tree[node.right])

def inorder(node):
  if node.left != '.':
    inorder(tree[node.left])
  print(node.value, end='')
  if node.right != '.':
    inorder(tree[node.right])

def postorder(node):
  if node.left != '.':
    postorder(tree[node.left])
  if node.right != '.':
    postorder(tree[node.right])  
  print(node.value, end='')

n = int(sys.stdin.readline())
tree = {}

for i in range(n):
  node, left, right = map(str, sys.stdin.readline().split())
  tree[node] = Node(node, left, right)


preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])

