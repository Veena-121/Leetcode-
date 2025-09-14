#brute force

arr = [-1,2,-3,4,5]

maxsum = float('-inf')
n= len(arr)

for i in range(0,n):
    currsum = 0;
    for j in range (i,n):
        currsum = currsum+arr[j]
        maxsum = max(maxsum,currsum)
        
print(maxsum)

#kadane's algo

c=0
m=float('-inf')
for i in range(n):
    
    c += arr[i]
    m = max(m,c)
    
    if c<0:
        c=0
print(m)
    
        