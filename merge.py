#merge sort
def merge(arr):
    n = len(arr)
    if n == 0 or n ==1:
        return arr
    m = n//2
    left = merge(arr[:m])
    right = merge(arr[m:])
    
    result =[]
    i=j=0
    
    while i<len(left) and j< len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

arr = [-38, 27, -43, 3, 9, 82, 10]
print("Sorted:", merge(arr))
            
    
    