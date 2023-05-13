# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
import math 


def searchInsert(self, nums: list[int], target: int) -> int:

    left = 0
    right = len(nums)
    mid = 0

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target: 
            left = mid + 1

        elif nums[mid] > target: 
            right = mid - 1

        else: # perfect case
            return mid
            
        
