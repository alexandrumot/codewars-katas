def find_nb(m):
    sum = 0
    n = 1
    while sum < m:
        sum += n*n*n
        if sum == m:
            return n
        n += 1 
    return -1




# Time Complexity - O(n)
# Space Complexity - O(n)