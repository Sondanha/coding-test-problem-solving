def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key=lambda x: x*3, reverse=True)
    result = ''.join(str_numbers)
    
    return '0' if result[0] == '0' else result











