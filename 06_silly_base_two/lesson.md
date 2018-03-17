# “Silly” Base Two
```
def silly_base_two(num):
```

We want to find the input in *binary* and return that binary representation as a “string” of ones and zeroes. Just like in **Reverse Digits**, the integer we return isn’t supposed to be interpreted as just one big number, but like a string of digits.

Base two (“binary”) is just a way to write down real values, just like the more familiar base ten (“decimal”). In base ten, each place (ones, tens, hundreds, etc.) corresponds with a power of ten. In base two, each place (ones, twos, fours, etc.) corresponds with a power of two.

For example, the number “twelve” is represented as “12” in base ten, but as “1100” in base two!
Examples:
```
>>> silly_base_two(0)
0
>>> silly_base_two(1)
1
>>> silly_base_two(2)
10
>>> silly_base_two(15)
1111
>>> silly_base_two(16)
10000
>>> silly_base_two(1234)
10011010010
```

*Fun Fact*: Computers use binary because it’s the overall best way for its hardware to store information. Inside your computer are billions of small electrical components that can either be in the “on” state or the “off” state. 
- Can you see how binary, made of symbols that are either in the “one” state or the “zero” state, might be a useful way to store data here? 
- What else do you have that can be in only one of two states? 
- Can you think of a way to count to 1024 using only 10 fingers?