#You are given a sorted array of integers nums and an integer target.
#Binary search’s job is to quickly find the position of a value in a sorted list.
#Return the index of the FIRST occurrence of target.
#If the target does not exist, return -1.

nums = [1, 2, 2, 2, 3, 4, 5]
target = 2



def occur(nums,target):
    left =0
    right = len(nums)-1
    result =-1  #stores the first occurrence if found
    while left<right:
        mid = (left+right)//2
        if nums[mid] == target:
            result= mid #at first you find target you stopbut now we have to keep going left to find fist occurence
            right = mid -1 #go left and find an earlier one
        elif nums[mid] < target:
            left +=1
        else :
            right+=1

    return result
    

print("output",occur(nums,target))



def finaloccur(nums,target):
    left =0
    right =len(nums)-1
    result =-1

    while left<=right:
        mid = (left +right)//2

        if nums[mid] == target:
            result =mid
            left = mid +1 #move to the right and find the closest one
        elif nums[mid]<target:
            left =mid+1
        else:
            right = mid -1

    return result

print("output",finaloccur(nums,target))

