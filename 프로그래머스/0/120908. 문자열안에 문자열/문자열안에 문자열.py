def solution(str1, str2):
    len_str2 = len(str2)
    for i in range(len(str1)-len_str2+1):
        if str2 == str1[i:i+len_str2]:
            return 1
    return 2