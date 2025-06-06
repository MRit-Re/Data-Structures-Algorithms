'''
O(n) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
'''

def palindrome_check(s):
    left,right = 0,len(s)-1
    while left <= right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True

print(palindrome_check("A man, a plan, a canal: Panama"))