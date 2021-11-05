"""
Find the Median of a Number Stream


Design a class to calculate the median of a number stream. The class should have the following two methods:

insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

EX.
1. insertNum(3)
2. insertNum(1)
3. findMedian() -> output: 2
4. insertNum(5)
5. findMedian() -> output: 3
6. insertNum(4)
7. findMedian() -> output: 3.5

"""

import heapq


class MedianOfAStream:
  def __init__(self):
      pass

  def insert_num(self, num):
      pass

  def find_median(self):
      pass
      

medianOfAStream = MedianOfAStream()
medianOfAStream.insert_num(3)
medianOfAStream.insert_num(1)

def test_1():
    results = medianOfAStream.find_median(head)
    assert (results == 2)

medianOfAStream.insert_num(5)

def test_1():
    results = medianOfAStream.find_median(head)
    assert (results == 3)

medianOfAStream.insert_num(4)

def test_1():
    results = medianOfAStream.find_median(head)
    assert (results == 3.5)

