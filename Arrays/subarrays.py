'''
O(2^n) : TIME COMPLEXITY
O(n) : SPACE COMPLEXITY
'''

def subarrays(array,start,end,n):
    if start == n:
        return
    if start > end:
        subarrays(array,start+1,n,n)
    if start <= end:
        print(array[start:end+1:1])
        subarrays(array,start,end-1,n)

print(subarrays([6,7,4,3,5,2],0,5,6))