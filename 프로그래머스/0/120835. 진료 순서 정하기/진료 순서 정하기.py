def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    result = []
    for i in emergency:
        result.append(sorted_emergency.index(i)+1)
    return result