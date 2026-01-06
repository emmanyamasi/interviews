#a sliding window is a technique where you look ata subset(window)of elements in an array and move it step by step instead of restarting from scratch each time
#fixed size window - maximum size of subarray of size k
#average of k elements

#Find the maximum sum of a subarray of size k.

nums = [2,1,5,1,3,2]
k =3
#first window =[2,1,5] sum  = 8
#slide right remove 2 add 1 sum =7
#slide right again  remove 1 add 3  sum -9
#max sum =9


def max_subbarray_sum(nums,k):
    window_sum = sum(nums[:k])#sum of numbers in range
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] #new element
        window_sum -= nums[i-k]
        max_sum= max(max_sum,window_sum)
    return max_sum



print("maxsum",max_subbarray_sum(nums,k))