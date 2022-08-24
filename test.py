# def sort_array(arr):
#     def rule(item):
#         if item % 2 != 0:
            
#     arr.sort(key=rule)
#     print(arr)
    

    
def sort_array(data):     
    odds = iter(sorted(el for el in data if el % 2))
    return [next(odds) if el % 2 else el for el in data]
    
if __name__ == "__main__":
    print(sort_array([5, 3, 2, 8, 1, 4]))
    
    