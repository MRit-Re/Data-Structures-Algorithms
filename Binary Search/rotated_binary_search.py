'''
O(logn) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
'''

def rotated_binary_search(array,start,end,target):
    start,end = 0,len(array)-1
    while end >= start:
        middle = (end+start)//2
        if array[middle] == target:
            return middle
        elif array[middle] >= array[start]:
            if array[middle] > target >= array[start]:
                end = middle-1
            else:
                start = middle+1
        else:
            if array[middle] < target <= array[end]:
                start = middle+1
            else:
                end = middle-1
    else:
        return -1

print(rotated_binary_search([4,5,1,2,3],0,4,5))
print(rotated_binary_search([2,3,4,5,1],0,4,5))
