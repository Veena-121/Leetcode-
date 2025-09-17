#bubble sort

def bubble_sort(arr):
    flag = True
    n = len(arr)
    while flag:
        flag = False
        
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i] , arr[i+1] = arr[i+1] , arr[i]
                flag = True
                
                
    return arr

def main():
    print(bubble_sort([-5,5,3,6,-1,2,2,-7]))
    
    
            
if __name__ == "__main__":
    main()
        