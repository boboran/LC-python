"""
Given a list of non-negative numbers and a target integer k,
write a function to check if the array has a continuous subarray of size at least 2
that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""
class Solution:
    """
    Thoughts:
    1. similar to two sum
    2. store sumToIndex%k instead of sumToIndex

    Time: O(n) where n is length of nums
    Space: O(n)
    """
    def checkSubarraySum(self, nums: 'List[int]', k: 'int') -> 'bool':
        mm = dict()
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if k!=0:
                total %= k
            if i>0 and total==0:
                return True
            if total in mm and i-mm[total]>1:
                return True
            if total not in mm:
                mm[total] = i
        return False
