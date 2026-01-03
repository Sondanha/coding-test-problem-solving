# def solution(arr):
#     answer = []
#     answer.append(arr[0])
#     for idx in range(1,len(arr)):
#         if arr[idx] != answer[-1]:
#             answer.append(arr[idx])   
#     return answer

def solution(arr):
    stack = []
    for i in arr:
        if stack and stack[-1] != i:
            stack.append(i)
        if not stack:
            stack.append(i)
                
    return stack

            
    