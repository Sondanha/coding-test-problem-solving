import math

def solution(progresses, speeds):
    result = []
    myList = [math.ceil((100-x)/y) for x, y in zip(progresses, speeds)]
    stack = []
    
    for i in myList:
        if stack and i > max(stack):
            result.append(len(stack))
            stack.clear()

        stack.append(i)
    result.append(len(stack))
    
    return result