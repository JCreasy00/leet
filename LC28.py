# if needle is in haystack return index where it begins


def strStr(self, haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1

# another solution would be:
# return haystack.find(needle)
