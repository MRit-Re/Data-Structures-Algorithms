'''
O(n^2) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
INPLACE, ONLINE, STABLE
'''

def insertion_sort(array,n):
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
            else:
                break
    return array

print(insertion_sort([5,3,1,4,2],5))
