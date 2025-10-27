def solution(age):
    # a:97
    return ''.join([chr(int(c)+97) for c in str(age)])