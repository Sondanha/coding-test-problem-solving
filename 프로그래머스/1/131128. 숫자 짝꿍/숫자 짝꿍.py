from collections import Counter

def solution(X, Y):
    x, y = Counter(X), Counter(Y)

    cnt = Counter()
    for i in range(10):
        if x[str(i)]*y[str(i)] != 0:
            cnt[str(i)] = min(x[str(i)], y[str(i)])
    
    if not cnt:
        return "-1"
#     else:
#         answer = ''
#         for i in range(9,-1,-1):
#             answer += (str(i)*cnt[str(i)])
        
#         if int(answer) == 0:
#             return "0"
#         else:
#             return answer
 
    answer = ''.join(d * cnt[d] for d in reversed("0123456789"))
    return "0" if answer[0] == "0" else answer
