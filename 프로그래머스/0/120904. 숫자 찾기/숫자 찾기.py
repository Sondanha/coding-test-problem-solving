def solution(num, k):
    num_list = list(str(num))
    if str(k) in num_list:
        return num_list.index(str(k))+1
    return -1
    