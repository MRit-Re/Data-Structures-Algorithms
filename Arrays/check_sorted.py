# objective is to check whether a given array is sorted
# in a sorted array, the adjacent element will be either greater than or equal to the preceeding element
# for i-th element if i+1-th element is smaller at any index, then the array is not sorted
# an empty or single element array is always sorted
# the array is traversed once ie. linear complexity

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