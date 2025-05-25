'''
O(logn) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
'''

def min_rotated(array,start,end):
    while end > start:
        middle = (end+start)//2
        if array[middle] > array[end]:
            if array[middle] >= array[start]:
                start = middle+1
            else:
                end = middle
        else:
            end = middle
    return array[start]

print(min_rotated([4,5,6,7,0,1,2,3],0,7))