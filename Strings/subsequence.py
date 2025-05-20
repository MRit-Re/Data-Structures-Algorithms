'''
O(n) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
'''

def subsequence_check(s,t):
    sub = 0
    for i in t:
        if sub == len(s):
            return True
        if i == s[sub]:
            sub += 1
    if sub == len(s):
        return True
    return False

print(subsequence_check("abc","adgberichj"))