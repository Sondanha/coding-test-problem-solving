def solution(common):
    a_1, a_2, a_3 = common[0], common[1], common[2]
    n = len(common)
    
    if a_1 == a_2:
        return a_1
    elif a_2 - a_1 == a_3 - a_2:
        return a_1+n*(a_2 - a_1)
    else:
        return a_1*((a_2/a_1)**n)