class Solution:
    def single(self,nums):
        result =0
        
        for i in nums:
            result ^= i #xor in binary
            
        return result
    
    
def main():
    s =Solution()
    print(s.single([1,2,3,4,3,1,4,5,5]))
    
if __name__ == "__main__":
    main()