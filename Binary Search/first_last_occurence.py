def search_range(array,target):
    def search(checkleft,left,right):
        index = -1
        while left <= right:
            middle = (left+right)//2
            if array[middle] > target:
                right = middle-1
            elif array[middle] < target:
                left = middle+1
            else:  
                index = middle                  
                if checkleft:
                    right = middle-1
                else:
                    left = middle+1
        return index
    return [search(True,0,len(array)-1),search(False,0,len(array)-1)]

print(search_range([2,2,3,3,3,3,4,4],3))
    
            