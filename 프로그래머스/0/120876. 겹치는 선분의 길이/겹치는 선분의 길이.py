def solution(lines):
    answer = 0
    for i in range(-100,101,1):
        cnt = 0
        for x, y in lines:
            if x<i+1 and i<y: # x <= i,i+1 <=y 경우를 포함해야 함.
                cnt += 1
        if cnt>1:
            answer += 1
            
    return answer