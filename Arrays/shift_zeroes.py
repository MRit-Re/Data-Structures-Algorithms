# objective is to shift all zeroes to the end of an array while maintaining the relative order of the non-zero elements
# maintain the index where a non-zero element should be placed if encountered while traversing the array ie. the last non-zero element
# swap the non-zero element with the current appropriate position for it 
# arrays with none or single elements cannot be shifted and are returned as it is 
# the array is traversed once ie. linear complexity

'''
O(n) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
'''

def shift_zeroes(array,n):
    if n < 2:
        return array
    i = 0
    for j in range(n):
        if array[j] != 0:
            array[i],array[j] = array[j],array[i]
            i+= 1               
    return array

    

print(shift_zeroes([0,1,2,0,0,4,3,0,5,0],10))
