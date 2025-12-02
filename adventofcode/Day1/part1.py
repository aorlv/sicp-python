def solutionDayOne():
    pos = 50
    password = 0

    with open("/Users/avo/Study/python/adventofcode/Day1/input.txt") as file:
        for x in file:
            steps = int(x[1:])

            pos = (pos + steps) % 100 if x[0] == 'R' else (pos - steps) % 100
            
            password = checkForZero(pos, password)
    
    print(password)                
    return password

def checkForZero(position, password):
    if position == 0:
        password += 1
    
    return password

solutionDayOne()