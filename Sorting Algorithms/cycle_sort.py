'''
O(n^2) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
INPLACE, ONLINE, UNSTABLE
'''

def cycle_sort(array,n):
    for cyclenumber in range(n):
        current = array[cyclenumber]
        count = cyclenumber
        for i in range(cyclenumber+1,n,1):
            if array[i] < current:
                count += 1
        if count == cyclenumber:
            continue
        while current == array[count]:
            count += 1
        array[count],current = current,array[count]
        while count != cyclenumber:
            count = cyclenumber
            for i in range(cyclenumber+1,n,1):
                if array[i] < current:
                    count += 1
            while current == array[count]:
                count += 1
            array[count],current = current,array[count]
        
    return array

print(cycle_sort([3,1,2,5,3,4],5))