'''
O(logn) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
'''

def sqrt(x):
    left,right = 0,x+1
    while left < right:
        middle = left+(right-left)//2
        if middle*middle > x:
            right = middle
        else:
            left = middle+1
    return left-1

print(sqrt(8))