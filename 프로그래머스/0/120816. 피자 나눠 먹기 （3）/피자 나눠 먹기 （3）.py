import math
def solution(slice, n):
    # (slice*result)>=n 만족하는 result의 최솟값
    return math.ceil(n/slice)