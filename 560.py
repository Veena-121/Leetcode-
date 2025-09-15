#brute force
class Solution:
    def subarraysum(self, nums,k):
        n = len(nums)
        count =0
        
        for i in range(n):
            currsum=0
            for j in range(i,n):
                currsum +=nums[j]
                
                if (currsum ==k):
                    count +=1
                    
        return count
    
#optimal sol

from collections import defaultdict

class Solution1:
    def sub(self,num,k):
        
        count=0
        currsum=0
        p_sum= defaultdict(int)
        p_sum[0]=1
        
        for i in num:
            currsum +=i
            if(currsum-k) in p_sum:
                count +=p_sum[currsum-k]
                
            p_sum[currsum]+=1
            
        return count
    
    
def main():
    c =Solution()
    print(c.subarraysum([1,2,3,4,5,6,7],9))
    c1=Solution1()
    print(c1.sub([1,2,3,4,5,6,7],9))
    
if __name__=="__main__":
    main()
    