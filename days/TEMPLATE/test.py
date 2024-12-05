from utils.helpers import read_input
from .solve import puzzleA, puzzleB

def test(file, solution):
    puzzle = file.split('/')[-1].split('.')[0]
    test_data = read_input(file)
    test_result = puzzleA(test_data)

    print("================================")
    print(puzzle, end="\n\n")
    print("input:")
    print(test_data, end="\n\n")

    print("assert:")
    print(f"{solution} == {test_result}")
    print("================================")
    
    assert test_result == solution, f"{puzzle}: {test_result} != {solution}"

def test_puzzleA(solution):
    test('inputs/testA.txt', solution)

def test_puzzleB():
    test('inputs/testB.txt')