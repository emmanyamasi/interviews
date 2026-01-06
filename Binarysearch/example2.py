#works in a sorted array
#instead of checking every element check the middle and throw away half the array each time

#O(log n)time


#you are given a sorted arrray of integers nums  and an integet target
#if the target does not exist return -1

nums = [1, 3, 5, 7, 9, 11]
target = 5


def search(nums,target):
    left = 0
    right = len(nums)-1

    while left <right:
        mid =(left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] <target:
            left =mid+1
        else :
            right = mid-1

    return -1



print("output",search(nums,target))



