"""
Merge K Sorted Lists

Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.
"""
import heapq

class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

def return_result(head):
    curr = head
    results = []
    while curr:
        results.append(curr.value)
        curr = curr.next
    
    return results


def merge_lists(lists):
    pass


l1 = ListNode(2)
l1.next = ListNode(6)
l1.next.next = ListNode(8)

l2 = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

l3 = ListNode(1)
l3.next = ListNode(3)
l3.next.next = ListNode(4)

def test_1():
    results = merge_lists([l1, l2, l3])
    assert (return_result(results) == [1,2,3,4,6,6,7,8])