#given  ana rray of integers and a target return truee if any 2 numbers add up to the target


def sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] +nums[j] == target:
                return True
            
    return False


nums = [1,2,3,4,5]
target =8
print("output",sum(nums,target))