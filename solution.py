def solution(s):
    
    occurrences = {}
    
    for letter in s:
        if letter not in occurrences:
            occurrences[letter] = 1
        else:
            occurrences[letter] += 1
            
    for key, val in occurrences.items():
        if val == 1:
            return key
            
    return '_'
