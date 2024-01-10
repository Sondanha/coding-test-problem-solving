str = input()
answer = ''
for i in str:
    if i.isupper():
        answer += i.lower()
    else:
        i.upper()
        answer += i.upper()
        
print(answer)
    