#121 Best tiem to buy and sell stocks

from typing import List

class Solution:
    def max_profit(self,prices:List[int])->int:
        minn = float('inf')
        maxx = 0
        
        for i in prices:
            minn = min(i,minn)
            maxx = max(maxx , i-minn)
            
        return maxx
    
    
def main():
    m = Solution()
    print(m.max_profit([1,2,4,6,2,7,3,8]))
    
    
if __name__ == "__main__":
    main()
    