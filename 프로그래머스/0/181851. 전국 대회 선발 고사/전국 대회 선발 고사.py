def solution(rank, attendance):
    A = []
    r = 1
    while len(A) < 3:
        targetIdx = rank.index(r)
        if attendance[targetIdx]: 
            A.append(targetIdx);
        r += 1
        
    return (10000*A[0])+(100*A[1])+A[2]  