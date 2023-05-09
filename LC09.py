# Given an integer x, return true if x is a 
# palindrome, and false otherwise.

# palindrome = same forwards and backwards 


def isPalindrome(self, x: int) -> bool:
    inp = str(x)

    return inp == inp[::-1]



# set the type of our input int to str
# check if inp == inp reversed, returns true if so and false if not
    
