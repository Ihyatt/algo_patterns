"""
Middle of the LinkedList

Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

If the total number of nodes in the LinkedList is even, return the second middle node.
"""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
head = Node(1)


def get_middle(head):
    pass


def test_1():
    results = get_middle(head)
    assert (results == 1)

head.next = Node(2)

def test_2():
    results = get_middle(head)
    assert (results == 1)

head.next.next = Node(3)

def test_3():
    results = get_middle(head)
    assert (results == 2) 

head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

def test_3():
    results = get_middle(head)
    assert (results == 3) 