'''
O(n) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
'''

def remove_element(nums,val):
    n = len(nums)
    i = 0
    for j in range(n):
        if nums[j] != val:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
    return nums[0:i:1]

print(remove_element([2,4,3,1,5],3))