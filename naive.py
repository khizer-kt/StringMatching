import time

def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)

    start_time = time.time()

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i+j] == pattern[j]:
            j += 1
        if j == m:
            end_time = time.time()
            execution_time = end_time - start_time
            return i, execution_time
    
    end_time = time.time()
    execution_time = end_time - start_time
    return -1, execution_time

text = "Hello, world!"
pattern = "world"
index, time_taken = naive_search(text, pattern)
print(f"Pattern found at index {index} in {time_taken:.6f} seconds.") 
