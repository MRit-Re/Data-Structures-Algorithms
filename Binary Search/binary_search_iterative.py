'''
O(logn) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
'''

def binary_search(array,start,end,target):
    while end >= start:
        middle = (end+start)//2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            start = middle+1
        else:
            end = middle-1
    else:
        return -1

print(binary_search([1,2,3,4,5],0,4,1))