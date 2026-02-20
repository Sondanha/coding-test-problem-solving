def solution(n):
    i = 1
    j = 1
    while True:
        if j >= n or (n > j and n < j*(i+1)):
            return i
        i += 1
        j *= i