#2 pointers  when we use 2 index variables  and move them i a controlled way

#i need to compare characters 
#first character shouuld match last character
#so as the second character
  #“I’ll use two pointers: one starting at the beginning of the string and one at the end.
#I’ll compare characters while moving the pointers inward


#example



#l e v e l
#0 1 2 3 4

 #l =l
#e =e Palindrome ✔


def is_palindrome(s):
    left = 0
    right = len(s) - 1 #len s gives the number of characters -1

    while left < right: #keep looping as long the left poniter is before the right pointer- if we havent reached the middle
        if s[left] != s[right]:
            return False

        left += 1 #move the ponter to the right 
        right -= 1 #move the pointer to the left

    return True


s = 'level'
print("return", is_palindrome(s))
