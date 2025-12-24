def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    
    hset = set(nums)

    sorted_set = sorted(hset)
    for x in range(1, len(sorted_set)):
        if sorted_set[x] == sorted_set[x - 1] + 1:
            res += 1
        else:
            max_res = max(max_res, res)
            res = 1
    res = max(max_res, res)


longestConsecutive([1,2,6,7,8])
longestConsecutive([0,3,7,2,5,8,4,6,0,1])
longestConsecutive([1,0,1,2])