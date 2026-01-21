def solution(n):
    answer = []
    i = 1
    while i <= n:
        if n%i == 0:
            answer.append(i)
        i += 1
        
    return answer