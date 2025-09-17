#sliding window
class Solution:
    def maxx(self,nums,k):
        n = len(nums)
        currsum =0
        
        for i in range(k):
            currsum +=nums[i]
            
        max_avg = currsum/k
        
        for i in range(k,n):
            currsum += nums[i]
            currsum -= nums[i-k]
            
            avg = currsum/k
            max_avg= max(max_avg , avg)
            
        return max_avg
    
def main():
    m = Solution()
    print(m.maxx([1,12,34,54,10,9],4))
    
if __name__ == "__main__":
    main()