#The goal is to return the indices of two numbers in the array that add up to the target value of 9.

#I’m using an optimized O(n) solution because the brute-force approach has O(n²) time complexity.
#Brute force checks all possible pairs, which means it repeats comparisons and performs poorly in the worst case, especially for large inputs.

#The optimized solution iterates through the array once.
#For each number, it calculates the required complement and checks if it has already been seen.
#If not, the number is stored in a dictionary for future lookups.
#This reduces the time complexity to O(n) while using additional space, making it the optimal solution for large-scale inputs.



def two_sum(nums , target):
    seen ={} #allows  fast look up and insert
    
    for i, current in enumerate(nums):
        needed = target - current

        if needed in seen:
            return [seen[needed], i] #returns index of the first number and index of second number
        seen[current] = i


nums = [2,7,11,15]
target = 9
print("result ",two_sum(nums,target))
