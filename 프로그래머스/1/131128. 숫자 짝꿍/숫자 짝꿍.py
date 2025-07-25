from collections import Counter

def solution(X, Y):
    x, y = Counter(X), Counter(Y)

    cnt = Counter()
    for i in range(10):
        if x[str(i)]*y[str(i)] != 0:
            cnt[str(i)] = min(x[str(i)], y[str(i)])
    
    if not cnt:
        return "-1"
    # else:
    #     answer = ''.join(sorted(cnt.elements(), reverse=True))
    #     if int(answer) == 0:
    #         return "0"
    #     else:
    #         return answer
    
    
    return ''.join(sorted(cnt.elements(), reverse=True))
