import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def postorder(preorder, inorder):
  if len(preorder) == 0:
      return
  elif len(preorder) == 1:
      print(preorder[0], end=' ')
      return
  elif len(preorder) == 2:
      print(preorder[1], preorder[0], end=' ')
      return

  root = preorder[0]
  div = inorder.index(root)

  postorder(preorder[1:div+1], inorder[0:div])
  postorder(preorder[div+1:], inorder[div+1:])

  print(preorder[0], end=' ')



test_num = int(input())
for _ in range(test_num):
  node_num = int(input())
  preorder = list(map(int, input().split()))
  inorder = list(map(int, input().split()))
  postorder(preorder, inorder)
  print()