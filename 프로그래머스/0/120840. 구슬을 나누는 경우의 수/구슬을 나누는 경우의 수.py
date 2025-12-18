# from itertools import combinations

# def solution(balls, share):
#     answer = 0
#     for i in combinations(range(balls), share):
#         answer += 1
#     return answer

def solution(balls, share):
    return factorial(balls)/(factorial(balls-share)*factorial(share))
    
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
