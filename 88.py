from typing import List
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        ind = m+n-1 
        i =m-1 
        j=n-1

        while(i>=0 and j>=0):
            if A[i] > B[j]:
                A[ind] = A[i]
                ind-=1
                i-=1
                
            else:
                A[ind] =B[j]
                ind -=1
                j-=1

        while (j>=0):
            A[ind] = B[j]
            ind -=1
            j-=1
        return A

def main():
    m =Solution()
    print(m.merge([1,2,3,0,0,0],3,[5,6,7],3))
    
if __name__ == "__main__":
    main()