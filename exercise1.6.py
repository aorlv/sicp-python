def square(n):
    return n * n

def good_enough(guess, x):
    return abs(square(guess) - x) < 0.001

def average(x, y):
    return (x + y) / 2

def improve(guess, x):
    return average(guess, (x / guess))

def sqrt_iter(guess, x):
    if good_enough(guess, x):
        return guess
    else:
        return sqrt_iter(improve(guess, x), x)
        #sqrt_iter(improve(guess, x), x)                #аналог того, что описано в задаче, функция уйдет в рекурсию

sqrt_iter(9, 1)