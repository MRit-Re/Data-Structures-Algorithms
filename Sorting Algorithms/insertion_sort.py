# objective is to start with one element and sort a partial array when next element arrives
# with each iteration the array to be swapped is enhanced
# have to find the correct place for incoming elements ie. index 1 onwards as a single element array is already sorted (loop 1)
# partial array consists of the already sorted array and the new element at the rightmost
# start iterating from the right of the sorted array ie. i-1 (just before the new element) to 0 (loop 2)
# if the current iterated element of sorted array is greater than the element after it, swap the elements (loop 2)
# due to decreasing of j and the swapping, a swap only occurs between j which is always from the sorted array and j+1 which is always the new element (loop 2)
# if compared and j is not greater than j+1, means that partial array is sorted and a new element is added (next iteration of loop 1)

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
