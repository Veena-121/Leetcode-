#quick sort
def quick(arr):
    n = len(arr)
    if n <=1:
        return arr
    
    p = arr[-1]
    
    left = [x for x in arr[:-1] if x <=p]
    right = [x for x in arr[:-1] if x > p]
    
    left = quick(left)
    right = quick(right)
    
    return left + [p] +right
    
    
e = [-23,43,56,2,8,-87,66,-12,45]
print(quick(e))