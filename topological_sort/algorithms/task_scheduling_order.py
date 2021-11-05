"""
Tasks Scheduling Order

There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to find the ordering of tasks we should pick to finish all tasks.
"""

def find_order(tasks, prerequisites):
    pass



def test_1():
    results = find_order(3, [[0, 1], [1, 2]])
    assert (results == [0, 1, 2])

def test_2():
    results = find_order(3, [[0, 1], [1, 2], [2, 0]])
    assert (results == [])
    