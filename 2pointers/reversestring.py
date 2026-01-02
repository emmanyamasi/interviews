

def reverse(s):
    left = 0
    right = len(s) -1

    while left< right:
        s[left],s[right] = s[right],s[left]

        left +=1
        right -=1
    return s #return loop should be after the while loop is over
    
s = ["h","e"," l","l","o"]
print(reverse(s))
