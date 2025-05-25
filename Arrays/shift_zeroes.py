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
