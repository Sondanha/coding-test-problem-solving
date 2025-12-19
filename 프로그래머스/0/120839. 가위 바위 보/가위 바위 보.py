def solution(rsp):
    rsp = list(rsp)
    for i in range(len(rsp)):
        if rsp[i] == '2':
            rsp[i] = '0'
        elif rsp[i] == '5':
            rsp[i] = '2'
        else:
            rsp[i] = '5'
            
    return "".join(rsp)