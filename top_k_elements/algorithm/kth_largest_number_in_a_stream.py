"""
Kth Largest Number in a Stream

Design a class to efficiently find the Kth largest element in a stream of numbers.

The class should have the following two things:

The constructor of the class should accept an integer array containing initial numbers from the stream and an integer ‘K’.
The class should expose a function add(int num) which will store the given number and return the Kth largest number.
"""


import heapq

class KthLargestNumberInStream:
  def __init__(self, nums, k):
      pass

  def add(self, num):
      pass


kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)

def test_1():
    results = KthLargestNumber.add(6)
    assert (results == 5)
    
def test_2():
    results = KthLargestNumber.add(13)
    assert (results == 6)
    

def test_3():
    results = KthLargestNumber.add(4)
    assert (results == 6)


