#You are given an array of integers nums and an integer k.

#Find the maximum sum of any contiguous subarray of size k.

#in problems  where we are dealing with contigous  elements sliding windows lets us use previous  calculations
#

nums = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
k = 3


def maxsum_array(nums,k):
    window_slide =sum(nums[:k])#sum of elements in k
    maxsum = window_slide

    for i in range (k,len(nums)):
        window_slide += nums[i] #add the elements
        window_slide -= nums[i-k]
        maxsum = max(maxsum,window_slide)
    return maxsum

print("maxsum_array", maxsum_array(nums,k))
    


    