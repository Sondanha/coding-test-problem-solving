def solution(sizes):
    x, y = 0, 0
    for i in sizes:
        if max(i) > x:
            x = max(i)
        if min(i) > y:
            y = min(i)
        
    return x*y