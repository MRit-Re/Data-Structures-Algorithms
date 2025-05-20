'''
O(n.logn) : TIME COMPLEXITY (worst case: O(n^2))
O(n) : SPACE COMPLEXITY (best case: O(logn))
INPLACE, OFFLINE, UNSTABLE
'''

def partition(array,low,high):
    pivot = array[high]
    i = low-1
    for j in range(low,high):
        if array[j] < pivot:
            i += 1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[high] = pivot,array[i+1]
    return i+1


def quick_sort(array,low,high):
    if low < high:
        correct = partition(array,low,high)
        quick_sort(array,low,correct-1)
        quick_sort(array,correct+1,high)
        return array

print(quick_sort([5,3,1,4,2],0,4))