from collections import Counter
from functools import reduce
from operator import mul  

def solution(clothes):
    # 의상 종류별 개수 세기
    values = list(Counter([i[1] for i in clothes]).values())

    # 여사건 계산: 전체 경우의 수 - 아무것도 안입는 경우    
    return reduce(mul,[i+1 for i in values]) - 1