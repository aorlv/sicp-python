def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        print("False")
        return False
    elif x < 10:
        print("True")
        return True

    tmp = x
    y = 0
    while tmp:
        y = y * 10 + tmp % 10
        tmp = tmp // 10
    
    if y == x:
        print("True")
        return True
    else:
        print("False")
        return False

isPalindrome(121)
isPalindrome(-123)
isPalindrome(10)