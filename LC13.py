# Given a roman numeral, convert it to an integer.


def romanToInt(self, s: str) -> int:
    '''Special cases to Consider
        IV, IX, XL, XC, CD, CM'''
    roman = 0
    myDict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
    }
    
    # Joining these together instead of having 6 individual replace commands is faster
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    
    for letter in s:
        roman += myDict[letter]

    return roman
                  


# the 'trick' to this problem is handling the subtraction cases
# ex. -> 9 == IX, 4 == IV, 40 == XL
# for all these cases we want to replace the two letter value with a long
#   extended very, for example 4 would turn into IIII

# at first I had 6 s = s.replace... lines but this was slower than joining
# them together and making 3
