def solution(s, skip, index):
    
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for c in skip:
        if c in alphabet: 
            alphabet.pop(alphabet.index(c))
    
    answer = []
    for c in s:
        answer.append(alphabet[(alphabet.index(c)+index)%len(alphabet)])
         
    return ''.join(answer)