from utils.helpers import read_input
from .solve import puzzleA, puzzleB


def test_puzzleA():
    testA_data = read_input('inputs/testA.txt')
    testA_sol = None
    testA_result = puzzleA(testA_data)
    print(testA_data, end="\n\n")
    print(f"{testA_sol} == {testA_result}")
    
    assert testA_result == testA_sol, f"{testA_sol} != {testA_result}"

def test_puzzleB():
    testB_data = read_input('inputs/testB.txt')
    testB_sol = None
    testB_result = puzzleB(testB_data)
    print(testB_data, end="\n\n")
    print(f"{testB_sol} == {testB_result}")
    
    assert testB_result == testB_sol, f"{testB_sol} != {testB_result}"

def run_tests():
    test_puzzleA()
    test_puzzleB()