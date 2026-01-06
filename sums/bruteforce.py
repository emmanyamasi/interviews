

def sum(nums, target):
    for i in range(len(nums)): #checks all possible pairs
        for j in range(i+1, len(nums)): #j is the second index used to loop through the list after i , i is pointing to one number  in the list
            if nums[i] +nums[j] == target:
                return [i,j] #return indexes


nums  = [2,7,11,15]
target = 9
print("Results", sum(nums,target))















