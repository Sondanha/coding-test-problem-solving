def solution(spell, dic):
    for s in dic:
        if len(s) == len(spell):
            for c in spell:
                s = s.replace(c, '', 1)
            if s == '':
                return 1                
    return 2