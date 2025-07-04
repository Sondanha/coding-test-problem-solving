def solution(participant, completion):
    sorted_parti = sorted(participant)
    sorted_compl = sorted(completion)
        
    for idx, c in enumerate(sorted_compl):
        if c != sorted_parti[idx] and c == sorted_parti[idx+1]:
            return sorted_parti[idx]
        
    return sorted_parti[-1]

# p = ['ana', 'mislav', 'mislav','mislav', 'stanko','stanko'] 
# c = ['ana', 'mislav', 'mislav','stanko','stanko']
