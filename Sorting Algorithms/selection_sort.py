'''
O(n^2) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
INPLACE, OFFLINE, UNSTABLE
'''

def selection_sort(array,n):
    for i in range(n):
        minimum = i
        for j in range(i+1,n):
            if array[minimum] > array[j]:
                minimum = j
        array[i],array[minimum] = array[minimum],array[i]
    return array

print(selection_sort([5,3,1,4,2],5))