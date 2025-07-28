def solution(answers):
    f, s, t = 0, 0, 0
    
    f_list = [1, 2, 3, 4, 5] 
    s_list = [2, 1, 2, 3, 2, 4, 2, 5] 
    t_list = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
        
    for idx, i in enumerate(answers):
        if i == f_list[idx%5]: f+= 1
        if i == s_list[idx%8]: s+= 1
        if i == t_list[idx%10]: t+= 1
    
    answer = []
    for idx,i in enumerate((f,s,t)):
        if i == max(f,s,t):
            answer.append(idx+1)
        
    return answer