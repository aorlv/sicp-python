def containsDuplicateBruteForce(nums):
    for i in range(len(nums)):
        for j in range(1 + i, len(nums)):
            if nums[i] == nums[j]:
                print("True")
                return True
    print("False")
    return False

def containsDuplicateSorting(nums):
    for i in range(len(nums) - 1):
        for j in range(1 + i, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            print("True")
            return True
    print("False")
    return False
    
def containsDuplicateHashset(nums):
    hashForTest = set()

    for num in nums:
        if num in hashForTest:
            print("True")
            return True
        hashForTest.add(num)

    print("False")
    return False
    

containsDuplicateBruteForce([1,2,3,1])
containsDuplicateBruteForce([1,2,3,4])
containsDuplicateBruteForce([1,1,1,3,3,4,3,2,4,2])

containsDuplicateSorting([1,2,3,1])
containsDuplicateSorting([1,2,3,4])
containsDuplicateSorting([1,1,1,3,3,4,3,2,4,2])

containsDuplicateHashset([3,3])
containsDuplicateHashset([1,2,3,4])
containsDuplicateHashset([1,1,1,3,3,4,3,2,4,2])

