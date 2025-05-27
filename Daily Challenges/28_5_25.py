'''
O(1) : TIME COMPLEXITY
O(1) : SPACE COMPLEXITY
'''

def differenceOfSums(n,m):
    total = (n*(n+1))//2
    div = 0
    if m <= n:
        x = n//m
        div = (x/2)*(2*m+((x-1)*m))
    return int(total-2*div)

print(differenceOfSums(10,3))