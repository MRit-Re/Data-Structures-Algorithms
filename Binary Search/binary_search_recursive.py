'''
O(logn) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
'''

def binary_search(array,start,end,target):
    if end >= start:
        middle = (end+start)//2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            return binary_search(array,middle+1,end,target)
        else:
            return binary_search(array,start,middle-1,target)
    else:
        return -1

print(binary_search([1,2,3,4,5],0,4,2))