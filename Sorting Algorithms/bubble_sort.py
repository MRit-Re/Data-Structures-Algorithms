'''
O(n^2) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
INPLACE, OFFLINE, STABLE
'''

def bubble_sort(array,n):
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array

print(bubble_sort([5,3,1,4,2],5))