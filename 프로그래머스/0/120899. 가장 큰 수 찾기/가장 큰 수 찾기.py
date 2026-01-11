def solution(array):
    max_num = sorted(array)[-1]
    return [max_num, array.index(max_num)]