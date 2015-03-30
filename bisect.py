def BiSector(number):
    low = 0.0
    high = number
    epsilon = 0.000001
    guess = (low + high) / 2
    
    while abs((number) - guess**2) > base:
        if guess**2 < number:
            high = guess
        elif guess**2 > number:
            low = guess
        elif guess**2 == number:
            