def solution(quiz):
    answer = []
    for i in quiz:
        str_list = i.split(' ')
        if eval(str_list[0]+str_list[1]+str_list[2]) == int(str_list[-1]):
            answer.append("O")
        else:
            answer.append("X")
        
    return answer