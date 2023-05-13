# https://leetcode.com/problems/remove-element/

def removeElement(self, nums: list[int], val,: int) -> int:

    i = 0
    count = 0 # count of good elements (elements != val)

    while (i < len(nums)):
        if nums[i] == val:
            nums.remove(nums[i])
        else:
            count +=1
            i += 1

    return count
            


# very simliar to LC26
# iterate through i
# if i == val remove it
# if not add to count
# return count
