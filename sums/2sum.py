#Given an array of integers nums and an integer target, return True if there exist two distinct numbers in the array whose sum is equal to target. Otherwise, return False.


def sum(nums , target):
     seen = set()

     for current  in nums:
          needed = target - current
          if needed in seen:
              return True
          
          seen.add(current)
     return False
          
#returns true or false
nums = [2,7,11,15]
target = 9
print("Result", sum(nums,target))   
       
       