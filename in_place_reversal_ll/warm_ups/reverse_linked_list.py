"""
Reverse a LinkedList 

Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.
"""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def return_list(head):
    curr = head
    results = []

    while curr:
        results.append(curr.value)
        curr = curr.next

def reverse_ll(head):
    pass




head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)

def test_1():
    reverse_ll(head)
    assert (return_list(head) == [10,8,6,4,2])