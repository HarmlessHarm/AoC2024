def reportIsSafe(report):

    listA = report[:-1]
    listB = report[1:]

    direction = listA[0] < listB[0]

    combined = list(zip(listA, listB))

    for i, (a, b) in enumerate(combined):
        if abs(a - b) > 3:
            return False
        if a == b:
            return False
        if (a < b) != direction:
            return False
        
    return True   

def puzzleA(data):

    return sum([reportIsSafe(list(map(int, line.split(' ')))) for line in data.split('\n')])
    
        
    
def puzzleB(data):
    
    total_safe = 0
    for line in data.split('\n'):
        report = list(map(int, line.split(' ')))
        safe = reportIsSafe(report)
        if safe:
            total_safe += 1        
        else:
            for i in range(len(report)):
                report2 = report[:i] + report[i+1:]
                safe2 = reportIsSafe(report2)
                if safe2:
                    total_safe += 1
                    break
 
    return total_safe