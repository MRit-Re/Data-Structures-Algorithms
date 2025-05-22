# objective is to find all the leader elements in a given array
# an element is a leader if and only if it is greater than all the elements to its right
# the rightmost element is always a leader as there are no elements to its right
# a variable tracks the current leader which is initially at the last index and traverses the list once from right to left
# if an element is greater than the current leader then it is also a leader and is added to the list and the current leader is also updated
# the array is traversed once ie. linear complexity

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
    return result

print(leaders([6,7,4,3,5,2],5))