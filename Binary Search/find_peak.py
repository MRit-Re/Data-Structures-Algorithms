def find_peak(array,left,right):
    while left < right:
        middle = (left+right)//2
        if array[middle] >= array[middle+1]:
            right = middle
        else:
            left = middle+1
    return left

print(find_peak([1,5,2,1,2],0,4))
