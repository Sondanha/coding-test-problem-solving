def solution(n):
    # 6과 n의 최소공배수
    if n%2 == 0 and n%3 != 0:
        return int(n/2)
    elif n%2 !=0 and n%3 == 0:
        return int(n/3)
    elif n%6 == 0:
        return int(n/6)
    return n