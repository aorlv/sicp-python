def isValid(s):
    if len(s) % 2 != 0:
        return False
    
    p_map = {')':'(', ']':'[', '}':'{'}
    verify = []
    
    for p in s:
        if p in p_map.values():
            verify.append(p)
        else:
            if not verify:
                return False
            if verify.pop() != p_map[p]:
                return False

    return not verify

isValid("()")
isValid("()[]{}")
isValid("(]")
isValid("([])")
isValid("([)]")

