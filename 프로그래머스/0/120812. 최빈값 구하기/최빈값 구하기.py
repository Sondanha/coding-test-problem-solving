from collections import Counter

def solution(array):
    num_list = Counter(array).most_common()
    if len(num_list) > 1 and num_list[0][1] == num_list[1][1]:
        return -1
    return num_list[0][0]