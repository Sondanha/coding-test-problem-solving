def solution(my_string):
    new_list = list(my_string)
    final_list = ''
    for i in new_list:
        if i not in final_list:
            final_list+=i

    return final_list