# objective is to generate all contigous subarrays of a given array
# we create arguments of start and end indices of the subarray and recursively decrese the end till it become less than start which means all the subarrays starting from this start are created 
# so when start > end, we generate the subarrays for start+1 till end = n and decrease end recursively till the process repeats
# when the start reaches value n it means that all subarrays have been generated and the function terminates
# each of the 2 recursion functions call themselves n times and hence exponential complexity

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