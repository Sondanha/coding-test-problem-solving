def solution(s): 
    stack = [] 
    result = []
    for idx, j in enumerate(s): 
        if not stack:
            stack.append(j)
            result.append(-1)
        else:
            if j not in stack:
                result.append(-1)
            else:
                result.append(idx - stack.index(j))
                stack[stack.index(j)] = 0 
            stack.append(j)
        
    return result