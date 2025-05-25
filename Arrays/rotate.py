'''
O(n) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
'''

def rotate(array,k):
        n = len(array)
        k %= n
        def reverse(array,start,end):
            while start < end:
                array[start],array[end] = array[end],array[start]
                start += 1
                end -= 1
        reverse(array,0,n-1)
        reverse(array,0,k-1)
        reverse(array,k,n-1)
        return array