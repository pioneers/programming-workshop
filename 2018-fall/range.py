#!/usr/bin/env python3

# You are given built-in functions max(a, b) and min(a, b).
# max(a, b) returns the greater of a and b.
# Similarly, min(a, b) returns the smaller of a and b.
#
# Examples:
#
#   >>> min(1, 2)
#   1
#   >>> min(2, 1)
#   1
#   >>> max(3, -1)
#   3

def range(a, b, c):
    # Return the statistical range of a set of three numbers.
    # This is the greatest of a, b, and c minus the smallest of
    # a, b, and c.
    #
    # Examples:
    #
    #   >>> range(4, 2, 1)  # 4 - 1
    #   3
    #   >>> range(3, -1, 2)  # 3 - (-1)
    #   4
    #
    # Hint: the maximum of three numbers a, b, and c is:
    #
    #   max(a, max(b, c))
    ...

def range_soln(a, b, c):
    return max(a, max(b, c)) - min(a, min(b, c))
