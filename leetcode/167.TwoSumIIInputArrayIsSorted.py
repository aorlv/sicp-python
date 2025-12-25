def twoSum(numbers, target):
    pl, pr = 0, len(numbers) - 1

    while pl < pr:
        tmp = numbers[pr] + numbers[pl]
        if tmp < target:
            pl += 1
        elif tmp > target:
            pr -= 1
        else:
            return [pl + 1, pr + 1]

twoSum([2,7,11,15], 9)
twoSum([2,3,4], 6)
twoSum([-1,0], -1)