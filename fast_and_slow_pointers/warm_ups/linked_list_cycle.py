"""
LinkedList Cycle

Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
"""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

def has_cycle(head):
    pass




def test_1():
    results = has_cycle(head)
    assert (results == False)

head.next.next.next.next.next.next = head.next.next

def test_2():
    results = has_cycle(head)
    assert (results == True)

head.next.next.next.next.next.next = head.next.next.next

def test_3():
    results = has_cycle(head)
    assert (results == True)   
