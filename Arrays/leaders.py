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