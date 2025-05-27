'''
O(n) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
'''

def merge(nums1,m,nums2,n):
    left,right,pointer = m-1,n-1,m+n-1
    while left >= 0 and right >= 0:
        if nums2[right] > nums1[left]:
            nums1[pointer] = nums2[right]
            right -= 1
        else:
            nums1[pointer] = nums1[left]
            left -= 1
        pointer -= 1
    while right >= 0:
        nums1[pointer] = nums2[right]
        right -= 1
        pointer -= 1
    return nums1

print(merge([1,2,3,0,0,0],3,[2,5,6],3))