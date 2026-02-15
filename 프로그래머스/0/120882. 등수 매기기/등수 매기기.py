def solution(score):
    sum_list = [sum(i)/2 for i in score]
    sorted_list = sorted(sum_list, reverse=True)
    
    return [sorted_list.index(i)+1 for i in sum_list]
