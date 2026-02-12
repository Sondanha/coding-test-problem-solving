import math
def solution(num, total):
    return [math.ceil(total/num-(num/2))+i for i in range(num)]