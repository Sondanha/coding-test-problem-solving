def solution(my_string):
    answer = []
    for i in my_string:
        n = int(ord(i))
        if n >= 48 and n <= 57:
            answer.append(int(i))
    return sorted(answer)