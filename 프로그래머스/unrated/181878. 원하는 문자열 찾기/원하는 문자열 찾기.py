def solution(myString, pat):
    new_myString = myString.lower()
    new_pat = pat.lower()
   
    return 1 if new_pat in new_myString else 0