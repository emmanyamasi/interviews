#given an array of sorted number determine if 2 numbers add up to the target value
#The point of two pointers is to reduce unnecessary work by using position and order instead of brute force. 
#allow me to solve array and string  problems  efficeintly by moving  through the data in a controlled way intead of nested loops
def sum_sorted(nums,target):
    left =0
    right = len(nums)-1
    while left <right:
        current_um = nums[left]+nums[right]
        if current_um == target:
          return True
        elif current_um <target:
           left +=1
        else:
           right -=1

    return False


nums = [1,2,4,6,10]
target = 10

print("output",sum_sorted(nums,target))
    
#since the array is sorted i used 2 pointers from both ends
#   this approach works because the array is  sorted  when the sum is too small movinf the left pointer increases it and when it it too large the right pointer decreases it
