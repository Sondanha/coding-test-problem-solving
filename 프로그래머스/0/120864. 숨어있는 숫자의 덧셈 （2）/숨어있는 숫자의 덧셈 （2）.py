def solution(my_string):
    num_list = []
    answer = 0
    for c in my_string:
        if c.isdigit(): # 숫자만
            num_list.append(c)
        elif num_list and c.isalpha(): # 문자만
            answer += int(''.join(num_list))
            num_list = []
            
    if num_list:  
        answer += int(''.join(num_list))
    return answer