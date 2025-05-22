# objective is to swap the largest elements at the end of the array
# with each iteration the array to be swapped is trimmed
# have to find the largest element n times to sort where n is the number of elements (loop 1)
# if the element to the left in a consecutive pair is larger it is moved to the right of the pair (loop 2)
# the swapping is performed n-i-1 times and at the end element at the n-i-1 index is found (loop 2)

'''
O(n) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
'''

def leaders(array,n):
    current = array[-1]
    result = [current]
    for i in range(-2,(n*-1)-1,-1):
        if array[i] > current:
            result.append(array[i])
            current = array[i]
    return result[-1::-1]

print(leaders([6,7,4,3,5,2],5))