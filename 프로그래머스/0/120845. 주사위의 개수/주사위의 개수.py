def solution(box, n):
    W = int(box[0]/n)
    L = int(box[1]/n)
    H = int(box[2]/n)
    
    return W*L*H