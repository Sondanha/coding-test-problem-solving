def solution(dots):
    s_dots = sorted(dots, key=lambda x:x[0])
    H = s_dots[1][1] - s_dots[0][1]
    W = s_dots[2][0] - s_dots[0][0]
    return H*W