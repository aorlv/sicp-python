def removeDuplicates(nums):
    k = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    k = len(nums) - k

    print(k)
    return k


removeDuplicates([1,1,2])
removeDuplicates([0,0,1,1,1,2,2,3,3,4])
