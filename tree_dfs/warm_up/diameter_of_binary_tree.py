"""
Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
"""

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def get_diameter(root):
    pass



treeDiameter = TreeNode()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

def test_1():
    results = get_diameter(head)
    assert (results == 5)



root.left.left = None
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)
root.right.right.left = TreeNode(9)
root.right.left.right.left = TreeNode(10)
root.right.right.left.left = TreeNode(11)

def test_2():
    results = get_diameter(head)
    assert (results == 7)