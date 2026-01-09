import math
def isDivisors(n):
    cnt_divisors = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            cnt_divisors += 1
        if cnt_divisors > 1:
            return True
    return False

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if isDivisors(i):
            answer += 1
    return answer