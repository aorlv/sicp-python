def square(n):
    return n * n

def good_enough(guess, x, oldguess = 0):
    print(guess, oldguess)
    if abs(oldguess - guess) < 0.001:
        return True
    
    oldguess = guess

def average(x, y):
    return (x + y) / 2

def improve(guess, x):
    return average(guess, (x / guess))

def sqrt_iter(guess, x, oldguess = 0):
    if good_enough(guess, x, oldguess):
        return guess
    else:
        return sqrt_iter(improve(guess, x), x, guess)

sqrt_iter(68, 23098)