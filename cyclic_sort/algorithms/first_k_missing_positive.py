"""
Find the First K Missing Positive Numbers

Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.
"""

def find_first_k_missing_positive(nums, k):
    missingNumbers = []
    out_of_range = set()
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = 0 

    for i in range(len(nums)):
        if not nums[i] or nums[i] == -float('inf'):
            continue
        index = abs(nums[i]) - 1
        if index >= len(nums):
            out_of_range.add(index + 1)
            continue
        nums[index] = abs(nums[index]) * -1 if nums[index] != 0 else -float('inf')

    for i in range(len(nums)):
        if nums[i] >= 0 and k:
            missingNumbers.append(i + 1)
            k -= 1
        i = i + 1
        while k:
            if i + 1 not in out_of_range:
            missingNumbers.append(i + 1)
            k -= 1
        i += 1
    return missingNumbers



def test_1():
    results = find_first_k_missing_positive([3, -1, 4, 5, 5], 3)
    assert (results == [1, 2, 6])

def test_2():
    results = find_first_k_missing_positive([2, 3, 4], 3)
    assert (results == [1,5,6])

def test_2():
    results = find_first_k_missing_positive([-2, -3, 4], 2)
    assert (results == [1, 2])
    