# def sort_array(arr):
#     def rule(item):
#         if item % 2 != 0:
            
#     arr.sort(key=rule)
#     print(arr)
    

    
def sort_array(source_array):     
    odds = iter(sorted(i for i in source_array if i % 2))
    return [next(odds) if i % 2 else i for i in source_array]
    
if __name__ == "__main__":
    print(sort_array([5, 3, 2, 8, 1, 4]))
    
    