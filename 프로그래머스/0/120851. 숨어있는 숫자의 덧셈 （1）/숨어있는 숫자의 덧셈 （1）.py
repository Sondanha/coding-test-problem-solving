def solution(my_string):
    answer = 0
    for i in my_string:
        n = int(ord(i))
        if n >= 48 and n <= 57:
            answer += int(i)
    return answer