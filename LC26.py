# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums: list[int]) -> int:
    # declare our counter and a set
    i = 0
    char = set()
    
    # while our counter is less than num of elements
    while (i < len(nums)):
        
        if (nums[i] in char): # case nums[i] is in the set already, should be removed
            nums.remove(nums[i])
            
        else: # case nums[i] isnt in the set, should be kept
            char.add(nums[i])
            i += 1
            
    return len(char)

# side note: we do not have to increase i in the first part of the if else
#            because removing an element advances the count and slides the next
#            element down
