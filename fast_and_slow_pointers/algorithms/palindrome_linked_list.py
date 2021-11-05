"""
Palindrome LinkedList


Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. 
he algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

"""

class Node:
  def __init__(self, value, next=None):
    self.val = value
    self.next = next



def is_list_palindrome(head):
    pass


head = Node(1)
def test_1():
    results = get_middle(head)
    assert (results == True)

head.next = Node(2)

def test_2():
    results = get_middle(head)
    assert (results == False)

head.next.next = Node(2)

def test_3():
    results = get_middle(head)
    assert (results == False) 

head.next.next.next = Node(1)

def test_3():
    results = get_middle(head)
    assert (results == True) 