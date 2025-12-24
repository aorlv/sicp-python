def removeDuplicates(nums):
    if not nums:
        return 0
    
    duplicates = 0
    length = len(nums)
    pl = 0

    for pr in range(1, length):
        if nums[pl] == nums[pr]:
            duplicates += 1
        else:
            nums[pl + 1] = nums[pr]  
            pl += 1

    answer = length - duplicates

    return answer

    
    

removeDuplicates([1,1,2])
removeDuplicates([0,0,1,1,1,2,2,3,3,4])
