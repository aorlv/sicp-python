def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    break
                if nums[j] == target - nums[i]:
                    print(i, j)
                    return i, j
                
twoSum([3,2,4], 6)
twoSum([2,7,11,15], 9)
twoSum([3,3], 6)
