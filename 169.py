#majority 
#boyer-moore TC:O(n) , SC:O(1)

class Solution:
    def maj(self,num):
        count =0
        candidate =None
        
        for i in num:
            if count==0:
                candidate =i
                
            count +=(1 if i== candidate else-1)
            
        return candidate
    
#hashmap TC:O(n) , SC:O(n)
from collections import Counter
class Solution1:
    def maj1(self,nums):
        count = Counter(nums)
        
        return max(count , key=count.get)
    
    
    
def main():
    m1 = Solution()
    print(m1.maj([1,2,2,2,2,2,3,4,5]))
    
    m2=Solution1()
    print(m2.maj1([1,2,2,2,2,2,3,4,5]))
    
if __name__ =="__main__":
    main()