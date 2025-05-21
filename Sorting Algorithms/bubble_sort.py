# objective is to swap the largest elements at the end of the array
# with each iteration the array to be swapped is trimmed
# have to find the largest element n times to sort where n is the number of elements (loop 1)
# if the element to the left in a consecutive pair is larger it is moved to the right of the pair (loop 2)
# the swapping is performed n-i-1 times and at the end element at the n-i-1 index is found (loop 2)

def bubble_sort(array,n):
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array

print(bubble_sort([5,3,1,4,2],5))