'''
O(n) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
'''

def product_except_self(nums):
        n = len(nums)
        array = [1]*n
        prefix,suffix = 1,1
        for i in range(n):
            array[i] *= prefix
            prefix *= nums[i]
            array[~i] *= suffix
            suffix *= nums[~i]
        return array