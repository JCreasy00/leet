# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# binary search is O(log n)

 
def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = 0

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target: 
                left = mid + 1

            elif nums[mid] > target: 
                right = mid - 1

            else: # perfect case
                return mid

        return left
            
