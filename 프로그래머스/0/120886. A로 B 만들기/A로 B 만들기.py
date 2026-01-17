def solution(before, after):
    bf = ''.join(sorted([i for i in before]))
    at = ''.join(sorted([i for i in after]))
    return 1 if bf == at else 0