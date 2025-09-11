#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range (len(nums)):
            for j in range (len(nums)):
                if i!=j and (nums[i]+ nums[j] == target):
                    l.append( [i,j]) #bit updation 

        return l
        
def main():
    s=Solution()
    nums = [2,3,4,5,6]
    target = 9
    result = s.twoSum(nums,target)
    print(result)
    
if __name__ == '__main__':
    main()
    