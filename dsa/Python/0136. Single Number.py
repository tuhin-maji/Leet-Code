"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""
#Approach-1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for x in nums:
            result=result^x
        return result
#Approach-2:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq_map = {}
        for i in range(len(nums)):
            if nums[i] in freq_map:
                freq_map[nums[i]]+=1
            else:
                freq_map[nums[i]]=1
        for num in freq_map:
            if freq_map[num]==1:
                return num
        
