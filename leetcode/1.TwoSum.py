def twoSum(nums, target):
        hmap = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hmap:
                return [i, hmap[diff]]
            hmap[nums[i]] = i
        
                
twoSum([3,2,4], 6)
twoSum([2,7,11,15], 9)
twoSum([3,3], 6)
