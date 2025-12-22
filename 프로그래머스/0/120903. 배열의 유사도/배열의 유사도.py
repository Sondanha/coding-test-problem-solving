from collections import Counter

def solution(s1, s2):
    return len(s1)-len(Counter(s1)-Counter(s2))