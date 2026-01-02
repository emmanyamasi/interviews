

def sum(nums, target):
    for i in range(len(nums)): #checks all possible pairs
        for j in range(i+1, len(nums)): #finds the sum
            if nums[i] +nums[j] == target:
                return [i,j]


nums  = [2,7,11,15]
target = 9
print("Results", sum(nums,target))















