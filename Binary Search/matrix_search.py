'''
O(logn) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
'''

def search_matrix(matrix, target):
        m,n = len(matrix),len(matrix[0])
        def element(x):
            return matrix[x//n][x%n]
        left,right = 0,m*n-1
        while left <= right:
            middle = left+(right-left)//2
            if element(middle) == target:
                return True
            elif element(middle) < target:
                left = middle+1
            else:
                right = middle-1
        return False

print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))