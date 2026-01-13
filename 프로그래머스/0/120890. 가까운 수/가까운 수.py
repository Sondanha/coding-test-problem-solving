def solution(array, n):
    array.append(n)
    array.sort()
    i = array.index(n)
    
    if i == 0:
        return array[1]
    elif i == (len(array)-1):
        return array[-2]
    else:
        if n-array[i-1] <= array[i+1]-n:
            return array[i-1]
        else:
            return array[i+1]