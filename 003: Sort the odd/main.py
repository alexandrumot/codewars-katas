def sort_array(source_array):     
    odds = iter(sorted(i for i in source_array if i % 2))
    
    result = []
    for i in source_array:
        if i % 2:
            result.append(next(odds))
        else:
            result.append(i)
    return result
