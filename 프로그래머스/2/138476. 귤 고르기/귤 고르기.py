from collections import Counter

def solution(k, tangerine):
    tan_list = sorted(Counter(tangerine).items(), key=lambda x : x[1], reverse=True)
    for i, t in enumerate(tan_list):
        k -= t[1]
        if k <= 0: 
            return i+1