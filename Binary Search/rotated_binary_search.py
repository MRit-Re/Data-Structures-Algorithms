# objective is to divide the given sorted array in halves and find the index of the target
# find the middle of the array and compare to the target
# if the middle is equal to the target then return middle, if the middle<target then the target can only be in the [middle+1..end] other wise in the [start...middle-1] subarray
# after determining the half in which the target is present, then edit the start or the end to perform the search on the subarray
# the function terminates when the target is found or when start > end and in that case -1 is returned
# each of the iterations reduces the size of the input and hence logarithmic complexity

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
