#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".



def longestCommonPrefix(self, strs: List[str]) -> str:

    i = 0
    temp = 0 
    toReturn = ""
    b = True
    smallest = 200

    for string in strs:
        if len(string) < smallest:
            smallest = len(string)
        

    while(b and i < smallest):
        currentChar = strs[0][i]
        for s in strs:
            if s[i] == currentChar:
                temp += 1

        if temp % len(strs) == 0:
            toReturn += currentChar
        else:
            b = False

        i += 1

    return toReturn                       

