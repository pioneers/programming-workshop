# Most Common Digit
```
def most_common_digit(num):
```

Find the most common digit in the input. Since there are arguably infinite zeroes to the right of every integer, we will not consider the digit zero.

*Special case*: if there is a tie between multiple digits, just return whichever digit has the largest numerical value. (e.g. if there are the same number of 1’s, 4’s, and 5’s, return 5.)

*Special case*: if we give you an integer that does not have any valid digits, just return the unmodified input.
Examples:
```
>>> most_common_digit(233)
3
>>> most_common_digit(33222)
2
>>> most_common_digit(2233)
3
>>> most_common_digit(12345)
5
>>> most_common_digit(9000000)
9
```