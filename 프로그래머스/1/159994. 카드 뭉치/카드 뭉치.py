def solution(cards1, cards2, goal):
    answer = 0
    cnt_1, cnt_2  = 0, 0
    for g in goal:
        if cnt_1 < len(cards1) and g == cards1[cnt_1]:
            answer += 1 
            cnt_1 += 1
        elif cnt_2 < len(cards2) and g == cards2[cnt_2]:
            answer += 1 
            cnt_2 += 1
        
    return "Yes" if answer == len(goal) else "No"