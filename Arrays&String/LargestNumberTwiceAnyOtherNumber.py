"""
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.
"""

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        largestpos = -1
        secondlargestpos = -1
        secondlargestVal = -1
        
        for i in range(0,len(nums)):
            if nums[i]==largest:
                largestpos = i
            elif nums[i]>secondlargestVal:
                secondlargestpos = i
                secondlargestVal = nums[i]
        
        if largest-(secondlargestVal*2)>=0:
            return largestpos
        
        return -1