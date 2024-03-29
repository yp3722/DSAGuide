"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumleft = 0
        sumright = sum(nums)-nums[0]
        
        if sumleft == sumright:
            return 0
        
        for i in range(1,len(nums)):
            sumleft+=nums[i-1]
            sumright-=nums[i]
            if sumleft == sumright:
                return i
        
        return -1