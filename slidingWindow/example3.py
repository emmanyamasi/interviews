#You are given an array nums representing the number of visitors to a website each day, and an integer k.

#Find the maximum number of visitors recorded over any k consecutive days.


nums = [10, 5, 2, 7, 8, 7]
k = 3


def maxsum(nums,k):
    windows_slide = sum(nums[:k])
    max_sum = windows_slide

    for i in range(k,len(nums)):
        windows_slide +=nums[i]#add elements
        windows_slide -=nums[i-k]
        maxsum = max(max_sum,windows_slide)

    return(maxsum)

print('maxsum',maxsum(nums,k))

