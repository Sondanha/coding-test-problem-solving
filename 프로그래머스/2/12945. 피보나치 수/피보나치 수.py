from collections import deque

def solution(n):
    dq = deque([0, 1])
    
    for i in range(n-1):
        num = sum(dq)
        dq.popleft()
        dq.append(num)
        
    return num%1234567

# def solution(n):
#     if n <= 1:
#         return n
#     else:
#         return (solution(n-1) + solution(n-2)) % 1234567