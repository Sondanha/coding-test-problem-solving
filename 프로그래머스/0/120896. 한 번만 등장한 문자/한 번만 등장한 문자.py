from collections import Counter
def solution(s):
    answer = []
    s_dict = Counter(s)
    for k, v in s_dict.items():
        if v == 1:
            answer.append(k)
    return ''.join(sorted(answer))