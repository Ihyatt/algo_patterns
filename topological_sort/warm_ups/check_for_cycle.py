"""
Given a graph, check if there is a cycle

"""

def check_cycle(edges):
    pass


def test_1():
    results = check_cycle([[0,1], [1,0]])
    assert (results == True)
    
def test_2():
    results = check_cycle([[0,1], [1,2]])
    assert (results == False)
    
