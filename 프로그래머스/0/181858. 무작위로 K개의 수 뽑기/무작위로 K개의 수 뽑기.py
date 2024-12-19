def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer and len(answer) < k:
            answer.append(i)
    if len(answer) < k:
        answer += [-1 for _ in range(k-len(answer))]
    return answer