from typing import List

from collections import deque

class Node:
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None


def create_tree(nums: List[int]):
  root = Node(nums[0])

  # BFS
  # nums = [1, 2, 3, 4, 5, 6, 7]
  i = 1

  Q = deque()
  Q.append(root)

  # Q: [1', 2', 3', 4', 5', 6', 7']
  while len(Q) > 0:
    node = Q.popleft()

    if i < len(nums):
      node.left = Node(nums[i])
      Q.append(node.left)
      i += 1

    if i < len(nums):
      node.right = Node(nums[i])
      Q.append(node.right)
      i += 1

  return root
    
def print_tree(node: Node):
  if node is None:
    return

  # pre-order
  # print(node.val)

  print_tree(node.left)

  # in-order
  # print(node.val)

  print_tree(node.right)

  # # post-order
  print(node.val)

  
def test():
  # nums = [1, 2, 3, 4, 5, 6, 7, None, None, 8]
  nums = [1, 2, 3, 4, 5, 6, 7]

  root = create_tree(nums)

  print("The tree:")
  print_tree(root)
  

test()
