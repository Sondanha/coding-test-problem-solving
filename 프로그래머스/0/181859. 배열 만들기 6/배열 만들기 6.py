def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif stk[-1] == arr[i]:
            stk.pop()
            i += 1
        else:
            stk.append(arr[i])
            i += 1
            
    return [-1] if stk == [] else stk