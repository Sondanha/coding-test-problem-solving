from collections import Counter

def solution(nums):
    if len(nums)/2 >= len(Counter(nums)): 
        return len(Counter(nums))
    else: 
        return len(nums)/2