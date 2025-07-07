def solution(phone_book):
    phone_book.sort() 
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

# def solution(phone_book):
#     for i in phone_book:
#         pre =''
#         for j in i[:-1]: # 자기 자신은 제외하고 찾음
#             pre += j
#             if pre in phone_book:
#                 return False
#     return True
        


