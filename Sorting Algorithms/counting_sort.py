'''
O(n^2) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
INPLACE, ONLINE, UNSTABLE
'''

def counting_sort(array,n):
    i = 0
    current = array[i]
    while i < n:
        count = 0
        for j in range(n):
            if array[j] < current:
                count += 1
        if current == array[count]:
            i += 1
            if i < n:
                current = array[i]
            print(array,i)
        else:
            temp = array[count]
            array[count] = current
            current = temp
            print(array)
    return array

print(counting_sort([3,1,2,5,4],5))