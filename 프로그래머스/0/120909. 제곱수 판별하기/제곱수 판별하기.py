import math 

def solution(n):
    raw_num = math.sqrt(n)
    int_num = int(raw_num)
    if raw_num > int_num:
        return 2
    else:
        return 1