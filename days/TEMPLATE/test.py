from utils.helpers import read_input
from .solve import puzzleA, puzzleB

def test(puzzle, file, solution = None):
    test_name = file.split('/')[-1].split('.')[0]
    test_data = read_input(file)
    if test_data == "":
        file = file.replace("B", "A")
        test_data = read_input(file)
    test_result = puzzle(test_data)

    print("================================")
    print(test_name, end="\n\n")
    if (solution):
        print("input:")
        print(test_data, end="\n\n")
        
        print("assert:")
        print(f"{solution} == {test_result}", end="\n\n")
        assert test_result == solution, f"{test_name}: {test_result} != {solution}"
    
        print(f"{test_name}: OK!")
    else:
        print(f"{test_name}: {test_result}")
    print("================================", end="\n\n")

def test_puzzleA(solution):
    test(puzzleA, 'inputs/testA.txt', solution)

def test_puzzleB(solution):
    test(puzzleB, 'inputs/testB.txt', solution)

def solve_puzzleA():
    test(puzzleA, 'inputs/puzzleA.txt')

def solve_puzzleB():
    test(puzzleB, 'inputs/puzzleB.txt')
