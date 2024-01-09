def solution(arr):
   
    if 2 in arr:
        fisrt2_index = arr.index(2) 
        re_last2_index = arr[::-1].index(2)
        last2_index = len(arr)-1-arr[::-1].index(2)
        answer = arr[fisrt2_index:last2_index+1]
    else:
        answer = [-1]
    
    return answer