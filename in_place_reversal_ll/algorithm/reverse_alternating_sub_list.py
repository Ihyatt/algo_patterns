"""
Reverse alternating K-element Sub-list


Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.
If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
"""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def return_list(head):
    results = []
    curr = head
    while curr:
        results.append(curr.value)
        curr = curr.next
    return results

def reverse_alternating(head, k):
    pass


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

def test_1():
    reverse_alternating(head, 3)
    assert (return_list(head) == [3, 2, 1, 4, 5, 6, 8, 7])

