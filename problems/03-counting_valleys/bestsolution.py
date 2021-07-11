def countingValleys(steps, path):

    valley = 0
    sea_level = 0
    for step in path:
        if step == 'U':
            sea_level += 1
        else:
            sea_level -= 1
            
        if sea_level == 0 and step == 'U':
            valley += 1 
            
    return valley
