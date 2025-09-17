#insertion sort
def ins(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i ,0 ,-1):
            if arr[j] < arr[j-1]: #ascending
                arr[j] , arr[j-1] = arr[j-1] , arr[j]
            else:
                break
            
    

def main():
    a=[-3,-7,1,6,5,3,9,-5,0,-2]
    ins(a)
    print(a)
    
if __name__ == "__main__":
    main()