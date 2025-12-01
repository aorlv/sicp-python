def square(n):
    return n * n

def improve(guess, x):
    return ((x / square(guess) + 2 * guess) / 3)

def good_enough(guess, oldguess = 0):
    print(guess, oldguess)
    if abs(oldguess - guess) < 0.001:
        return True
    oldguess = guess

def cube_root(guess, x, oldguess = 0):
    if good_enough(guess, oldguess):
        return guess
    else:
        return cube_root(improve(guess, x), x, guess)
    
cube_root(4, 4322)

print(16.289018662718114 * 16.289018662718114 * 16.289018662718114)