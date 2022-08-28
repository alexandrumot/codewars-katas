def beeramid(bonus, price):
    counter = 0

    while bonus >= (counter+1)*(counter+1)*price:
        counter += 1
        bonus -= counter*counter*price
        
    return counter




# Time Complexity - O(n)
# Space Complexity - O(n)