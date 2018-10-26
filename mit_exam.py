def longestRun(L):
    index = 0
    longest_run = 0
    while index < len(L)-1:
        current = index
        next_int = index + 1
        len_run = 1
        stillRun = True
        while stillRun and next_int < len(L)-1:
            if L[next_int] < L[current]:
                if len_run > longest_run:
                    longest_run = len_run
                stillRun = False
            else:
                current += 1
                next_int += 1
                len_run += 1
        index += 1
    return longest_run
