def solution(n):
    num_list = list(str(n))
    num_list.reverse()
    result = []
    for i in num_list:
        result.append(int(i))
        
    return result