def solution(s):
    answer = 0
    s_list = s.split(' ')
    for idx, i in enumerate(s_list):
        if i == 'Z':
            answer -= int(s_list[idx-1])
        else:
            answer += int(i)
            
    return answer