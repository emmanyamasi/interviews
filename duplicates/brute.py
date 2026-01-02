def duplicates(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)): #we want  j to start after i
            if nums[i] == nums[j]:
                return True
    return False
            


nums  = [1,2,3,1]
print("nums", duplicates(nums))
