'''
O(n) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
'''

def check_sorted(array,n):
    for i in range(n-1):
        if array[i] > array[i+1]:
            return False
    return True


print(check_sorted([6,7,4,3,5,2],5))