def solution(arr, flag):
    answer = []
    
    for idx, tf in enumerate(flag):
        if tf:
            for i in range(arr[idx]*2):
                answer.append(arr[idx])
        else: 
            answer = answer[:-arr[idx]]
    return answer
    