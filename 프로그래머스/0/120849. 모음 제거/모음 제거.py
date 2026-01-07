def solution(my_string):
    answer = ''
    for c in my_string:
        if not c in ['a','e','i','o','u']:
            answer += c
    return answer