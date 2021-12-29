def direction(facing, turn):
    compass = {
        'N':  0,
        'NE': 45,
        'E':  90,
        'SE': 135,
        'S':  180,
        'SW': 225,
        'W':  270,
        'NW': 315,
    }

    current_turn = 0
    try:
        current_turn = compass[facing]
    except KeyError:
        return(f"Wrong direction: {facing}; NO Such Direction Exists")
         
    if -1080 > turn or turn > 1080 or turn%45 != 0:
        return(f"Wrong turning degree: {turn}; Degree must be between (-1080; 1080) and be multiple of 45")
    
    new_turn = current_turn + turn
    while new_turn < 0:
        new_turn += 360
    while new_turn >= 360:
        new_turn -= 360
    
    try:
        new_direction = list(compass.keys())[list(compass.values()).index(new_turn)]
    except ValueError:
        return(f"{new_turn} is not possible result; no direction with such degree exists")
        
    return new_direction
