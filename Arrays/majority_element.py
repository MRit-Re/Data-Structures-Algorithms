def majority_element(array):
        count,major = 0,0
        for i in array:
            if count == 0:
                major = i
            if i == major:
                count += 1
            else:
                count -= 1
        return major

print(majority_element([1,1,2,2,2,1,1]))