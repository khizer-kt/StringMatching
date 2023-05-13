def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    table = partial_match_table(pattern)
    
    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                return i - j
        elif j > 0:
            j = table[j-1]
        else:
            i += 1
    
    return -1


def partial_match_table(pattern):
    m = len(pattern)
    table = [0] * m
    i = 1
    j = 0
    
    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
            i += 1
        elif j > 0:
            j = table[j-1]
        else:
            table[i] = 0
            i += 1
    
    return table 
