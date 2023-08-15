import math


def bs_list(haystack: list, needle: int) -> bool:

    lo = 0
    hi = len(haystack)

    while hi > lo:
        m = math.floor(lo + (hi - lo) / 2)
        v = haystack[m]
        if needle == v:
            return True
        elif v < needle:
            lo = m + 1
        else:
            hi = m

    return False
