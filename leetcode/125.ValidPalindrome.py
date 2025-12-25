def isPalindrome(s):
    if len(s) <= 1:
        return True
    
    pl, pr = 0, len(s) - 1

    while pl < pr:
        while pl < pr and not s[pl].isalpha() and not s[pl].isdigit():
            pl += 1
        while pr > pl and not s[pr].isalpha() and not s[pr].isdigit():
            pr -= 1
        
        if s[pl].lower() != s[pr].lower():
            return False
        pl += 1
        pr -= 1
    return True

    


isPalindrome("A man, a plan, a canal: Panama")
isPalindrome("0P")
isPalindrome("race a car")
isPalindrome(" ")