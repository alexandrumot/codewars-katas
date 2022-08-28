def score(dice):
    score = 0
    table = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }

    for i in dice:
        table[i] += 1
        
    for k, v in table.items():
        if v >= 3:
            v -= 3
            if k == 1:
                score += 1000
            else:
                score += k*100
        
    if table[1] != 0:
        score += table[1]*100
    if table[5] != 0:
        score += table[5]*50
    return score 