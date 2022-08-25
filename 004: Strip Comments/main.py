def strip_comments(strng, markers):
    markers = ''.join(markers)

    result = []
    for line in strng.split('\n'):
        for marker in markers:
            
            if marker in line:
                line = line.split(marker)[0].rstrip() 
        else:
            result.append(line.rstrip())
                
    return '\n'.join(result)