/*
169. Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

 */
import scala.collection.mutable
object Solution {
  def majorityElement(nums: Array[Int]): Int = {
    var map = mutable.Map.empty[Int, Int]

    nums.foreach(num => {
      if (map.contains(num)) {
        map.update(num, map(num) + 1)
      } else {
        map += (num -> 1)
      }
    })
    val majorityCount=(nums.length/2.0).floor
    var majorityElement=nums(0)
    for (num<- nums){
      if(map(num)>majorityCount){
        majorityElement=num
      }
    }
    return majorityElement
  }
}