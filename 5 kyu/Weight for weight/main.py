def order_weight(strng):
    sums = []
    for i in strng.split():
        # pushing the sum of digits
        sums.append(sum(list(map(int, i)))) 
    
    # converting string list to int list
    weights = list(map(int, strng.split())) 

    # basically I sort the (weights, sums) pairs list by:
    # 1. the sum
    # 2. alphabetically
    weights_sorted = [pair for pair in sorted(zip(weights, sums), key=lambda item: (item[1], str(item[0])))] 
    
    # converting weights back to string to join and return
    return ' '.join(list(map(str, [item[0] for item in weights_sorted]))) 




# Time Complexity - O(n)
# Space Complexity - O(n)