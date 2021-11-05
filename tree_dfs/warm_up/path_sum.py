"""
Path Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

"""

def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def get_sum(root):
    pass

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)



def test_1():
    results = get_sum(root, 23)
    assert (results == True)
