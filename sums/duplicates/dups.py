
#given an array  of integers return true if any value appears  more than once return false else
#we used optimized o because it stores in a set the data and  is fast as it checks n only once as compared to brute which compares two values

def  duplicates(nums):
     seen = set()
     for num in nums:
          if num in seen:
               return True
          seen.add(num)
     return False

nums = [1,3,4,1]
print("Output",duplicates(nums))