def sel(arr):
    n= len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
            
        arr[i] , arr[min_index] = arr[min_index] , arr[i]
        
c = [-3,-7,1,6,5,3,9,-5,0,-2]
sel(c)
print(c)
        