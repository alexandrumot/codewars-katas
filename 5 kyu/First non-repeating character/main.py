def first_non_repeating_letter(string):
    table = {}
    for i in string:
        table[i.lower()] = 0
    for i in string:
        table[i.lower()] += 1
    for i in string:
        if table[i.lower()] == 1:
            return i
    return ''




# Time Complexity - O(n)
# Space Complexity - O(n)       