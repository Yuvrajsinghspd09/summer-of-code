def rev_string(s):
    left,right = 0,len(s)-1
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return s
#practice attempt 1
def rev_string(s):
    left=0
    right=len(s)-1
    while left<right:
        s[left],s[right] =s[right],s[left]
        left+=1
        right-=1
    return s
