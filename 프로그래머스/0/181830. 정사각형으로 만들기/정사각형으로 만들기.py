def solution(arr):
    answer = [[]]
    [rows, cols] = getRowNCol(arr)
    
    while rows < cols:
        addOneRow(arr, cols)
        [rows, cols] = getRowNCol(arr)
        
    while cols < rows:
        addOneColumn(arr)
        [rows, cols] = getRowNCol(arr)
    
    return arr

def getRowNCol(arr):
    return [len(arr), len(arr[0])]

def addOneColumn(arr):
    for i in arr:
        i.append(0)
        
def addOneRow(arr, cols):
    arr.append([0 for i in range(cols)])
    