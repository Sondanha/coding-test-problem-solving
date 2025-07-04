# def solution(participant, completion):
#     sorted_parti = sorted(participant)
#     sorted_compl = sorted(completion)
        
#     for idx, c in enumerate(sorted_compl):
#         if c != sorted_parti[idx] and c == sorted_parti[idx+1]:
#             return sorted_parti[idx]
        
#     return sorted_parti[-1]

def solution(participant, completion):
    sorted_parti = sorted(participant)
    sorted_compl = sorted(completion)
        
    for p, c in zip(sorted_parti, sorted_compl):
        if p != c:
            return p
    return sorted_parti[-1]

