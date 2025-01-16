"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        flag=0

        for num in nums:
            if num!=0:
                product=product*num
            else:
                flag+=1
        for i in range(len(nums)):
            if flag==0:
                nums[i]=product//nums[i]
            elif flag==1:
                if nums[i]==0:
                    nums[i]=product
                else:
                    nums[i]=0
            else:
                nums[i]=0
        return nums
