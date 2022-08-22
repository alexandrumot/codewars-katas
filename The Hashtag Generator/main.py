def generate_hashtag(s):
    if s == '' or len(s) > 140:
        return False
        
    arr = [i.capitalize() for i in s.split(' ')]
    
    return '#' + ''.join(arr) 