from collections import deque

def solution(priorities, location):
    dq = deque([(idx,p) for idx, p in enumerate(priorities)])
    p_dq = deque(priorities)
    result=[]
    
    while len(dq)>0:
        if dq[0][1] < max(p_dq): 
            dq.append(dq.popleft()) 
            p_dq.append(p_dq.popleft())
        else:
            result.append(dq.popleft())
            p_dq.popleft()
            
    for i in range(len(result)): 
        if result[i][0] == location:
            return i+1








