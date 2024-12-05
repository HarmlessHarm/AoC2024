from utils.helpers import read_input

def puzzleA(data):
    lines = data.split("\n")
    lines = [list(map(int, line.split('   '))) for line in lines]
    listA, listB = zip(*lines)
    sortedZip = zip(sorted(listA), sorted(listB))
    distanceList = [abs(a - b) for a, b in sortedZip]
    return sum(distanceList)

def puzzleB(data):
    return Exception("Not implemented")