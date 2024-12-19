def solution(myStr):
    myStr = myStr.replace("b","a")
    myStr = myStr.replace("c","a")
    
    myStr = myStr.split('a')
    answer = [i for i in myStr if i != ""]
    return ["EMPTY"] if len(answer) == 0 else answer