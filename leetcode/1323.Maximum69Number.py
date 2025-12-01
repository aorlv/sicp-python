def maximum69Number (num: int) -> int:
    if num == 9999:
        print(num)
        return num
    
    helper = 1000

    while helper >= 1:
        if num // helper % 10 == 6:
            num += helper * 3
            num = int(num)
            break
        helper /= 10
    
    """
    for helper in [1000, 100, 10, 1]:
        if num // helper % 10 == 6:
            num += helper * 3
            num = int(num)
            break
    """
            
    print(num)
    return num

maximum69Number(6969)
maximum69Number(9969)
maximum69Number(9996)
