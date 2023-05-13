# https://leetcode.com/problems/plus-one/
# intListToNum.py in usefulThings repo


def plusOne(self, digits: list[int]) -> list[int]:
    # intListToNum - turn an array of ints to a single int -> [1,2,3] = 123
    numSum = 0
    count = len(digits) - 1

    for i, num in enumerate(nums):
        numSum += num * 10 ** count
        count -= 1

    # adding one and then turning back into an array of intsf
    numSum += 1 # the problem wants us to increase buy 1
    numSum = str(numSum) # change to a string so it is iterable
    output = []

    for i in numSum: # for each char in the string add the int version to output
        output.append(int(i))

    return output

    
