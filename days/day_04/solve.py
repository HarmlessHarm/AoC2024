import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

def rotate90(array):
    return np.flip(array.T, axis=1)

def rotate45(array):
    n1, n2 = array.shape
    newList = []
    for k in range(n1+n2-1):
        newList.append([])
        for i in range(k+1):
            j = k-i
            if i < n1 and j < n2:
                newList[k].append(str(array[i,j]))
        newList[k] = ''.join(newList[k])

    return np.array(newList)

def countXMAS(array):
    stringArray = np.array([''.join(L) for L in array.tolist()])
    return np.strings.count(stringArray , 'XMAS').sum()

def puzzleA(data):
    array = np.array([list(line) for line in data.split('\n')])

    array90 = rotate90(array)
    array180 = rotate90(array90)
    array270 = rotate90(array180)

    array45 = rotate45(array)
    array135 = rotate45(array90)
    array225 = rotate45(array180)
    array315 = rotate45(array270)
   
    arrays = [array, array90, array180, array270, array45, array135, array225, array315]
    counts = [countXMAS(a) for a in arrays]
    return sum(counts)

def isXMAS(window):
    if window[1,1] != 'A':
        return False
    
    diagTLBR = window[0,0] == 'M' and window[2,2] == 'S'
    diagTRBL = window[0,2] == 'M' and window[2,0] == 'S'
    diagBLTR = window[2,0] == 'M' and window[0,2] == 'S'
    diagBRTL = window[2,2] == 'M' and window[0,0] == 'S'

    combinations = [diagTLBR and diagTRBL, diagTLBR and diagBLTR, 
                    diagBRTL and diagTRBL, diagBRTL and diagBLTR]

    if sum(combinations) > 0:
        return True
    return False

def puzzleB(data):
    array = np.array([list(line) for line in data.split('\n')])

    windows = sliding_window_view(array, (3,3))
    windows = windows.reshape(-1, 3, 3)

    return sum([isXMAS(window) for window in windows])