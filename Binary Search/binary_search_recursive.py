# objective is to divide the given sorted array in halves and find the index of the target
# find the middle of the array and compare to the target
# if the middle is equal to the target then return middle, if the middle<target then the target can only be in the [middle+1..end] other wise in the [start...middle-1] subarray
# after determining the half in which the target is present, then recursively perform the search on the subarray
# the function terminates when the target is found or when start > end and in that case -1 is returned
# each of the recursion functions reduces the size of the input and hence logarithmic complexity

'''
O(logn) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
'''

def binary_search(array,start,end,target):
    if end >= start:
        middle = (end+start)//2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            return binary_search(array,middle+1,end,target)
        else:
            return binary_search(array,start,middle-1,target)
    else:
        return -1

print(binary_search([1,2,3,4,5],0,4,2))