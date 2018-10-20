#!/usr/bin/env python3

# Create a function is_leap_year(year) that determines whether
# the given year is a leap year.
#
# A year is a leap year if the year is divisible by four and
# the year is not divisible by 100. However, years divisible
# by 400 are leap years, and are an exception to the 100-year
# rule.
#
# Examples:
#
#   >>> is_leap_year(301)
#   False
#   >>> is_leap_year(304)
#   True
#   >>> is_leap_year(300)
#   False
#   >>> is_leap_year(400)
#   True
#
# Hint: "a % b" calculates the remainder of dividing a by b,
#       so "a % b == 0" is true if a is divisible by b.

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
