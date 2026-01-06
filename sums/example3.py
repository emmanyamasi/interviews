#given an array of integers and a target sum find 2 numners in the array that add up to the target ,return their indices you can  assume there is exactly one solution and you cant use the same element twice


nums = [1,2,3,4,5]
target =9

def find(nums,target):
    for i in range(len(nums)):#check existence of numbers in nums
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return([i,j])
            



print("output",find(nums,target))