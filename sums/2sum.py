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
       
       