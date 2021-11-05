"""
Connect Level Order Siblings

Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.
"""
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

def return_level(root):
    pass

def connect_traversal(root):
    if not root:
        return
    q = deque()
    q.append(root)
    while q:
        n = len(q)
        temp_q = deque()
        for _ in range(n):
            node = q.popleft()
            if node.left:
                temp_q.append(node.left)
            if node.right:
                temp_q.append(node.right)
      
            node.next = q[0] if q else None

        q.extend(temp_q)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

def test_1():
    results = connect_traversal(root)
    assert (results == [[12], [7, 1], [9, 10, 5]])


