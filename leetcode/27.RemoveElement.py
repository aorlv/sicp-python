def removeElement(nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
    
"""
    index = []
    for i in range(len(nums)):
        if nums[i] == val:
            index.append(i)

    index.sort(reverse=True)

    for k in index:
        nums.pop(k)
            
    print(len(nums))
    return len(nums)
"""
    



removeElement([3,2,2,3], 3)
removeElement([0,1,2,2,3,0,4,2], 2)