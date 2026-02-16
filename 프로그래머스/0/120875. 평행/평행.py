def solution(dots):
    
    def cal_gradient(list1, list2):
        x1, y1, x2, y2 = list1[0], list1[1], list2[0], list2[1]
        if (y2-y1) == 0:
            return 1
        return (x2-x1)/(y2-y1)
    
    if cal_gradient(dots[0], dots[1]) == cal_gradient(dots[2], dots[3]):
        return 1
    elif cal_gradient(dots[0], dots[2]) == cal_gradient(dots[1], dots[3]):
        return 1
    elif cal_gradient(dots[0], dots[3]) == cal_gradient(dots[1], dots[2]):
        return 1
    
    return 0