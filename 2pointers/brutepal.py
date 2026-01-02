 


def ispal(s):
    for i in range(len(s)):
 
            if s[i] != s[len(s)-1-i]:
                  return False
            
    return True





s = 'level'
print("output",ispal(s))