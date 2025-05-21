# objective is to select the minimum element and place them sequentially at the correct index
# with each iteration the array to be checked for minimum is trimmed
# have to find the smallest element n times to sort where n is the number of elements (loop 1)
# if the current minimum element is larger than current element, minimum element is changed (loop 2)
# minimum element is placed at the i-th position at the end (loop 2)
# the array checked decreses in size as with each iteration i-th minimum element is found (loop 2)

def selection_sort(array,n):
    for i in range(n):
        minimum = i
        for j in range(i+1,n):
            if array[minimum] > array[j]:
                minimum = j
        array[i],array[minimum] = array[minimum],array[i]
    return array

print(selection_sort([5,3,1,4,2],5))