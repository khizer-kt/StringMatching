import time

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    table = partial_match_table(pattern)

    start_time = time.time()

    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                end_time = time.time()
                execution_time = end_time - start_time
                return i - j, execution_time
        elif j > 0:
            j = table[j-1]
        else:
            i += 1

    end_time = time.time()
    execution_time = end_time - start_time
    return -1, execution_time


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

# Test case
text = "Hello, world!"
pattern = "world"
index, time_taken = kmp_search(text, pattern)
print(f"Pattern found at index {index} in {time_taken:.6f} seconds.") 
