# objective is to divide the array in half till it reaches single elements and sort them one at a time while merging
# divide and conquer algorithm using recursion
# first the left half is seperated and sorted and then the right half and these are then merged
# merge function compares the left and right half elements and places them in the original array at the appropriate place

'''
O(n.logn) : TIME COMPLEXITY
O(n) : SPACE COMPLEXITY
OFFLINE, STABLE
'''

def merge(array,left,middle,right):
    n1 = middle-left+1
    n2 = right-middle
    leftCopy = [0]*n1
    rightCopy = [0]*n2
    for i in range(n1):
        leftCopy[i] = array[left+i]
    for i in range(n2):
        rightCopy[i] = array[middle+i+1]
    cnt,l,r = left,0,0
    while l < n1 and r < n2:
        if leftCopy[l] <= rightCopy[r]:
            array[cnt] = leftCopy[l]
            l += 1
        else:
            array[cnt] = rightCopy[r]
            r += 1
        cnt += 1
    while l < n1:
        array[cnt] = leftCopy[l]
        l += 1
        cnt += 1
    while r < n2:
        array[cnt] = rightCopy[r]
        r += 1
        cnt += 1


def merge_sort(array,left,right):
    if left < right:
        middle  = (left+right)//2
        merge_sort(array,left,middle)
        merge_sort(array,middle+1,right)
        merge(array,left,middle,right)
        return array

print(merge_sort([5,3,1,4,2],0,4))