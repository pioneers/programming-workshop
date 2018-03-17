# Reverse Digits

``` 
def reverse_digits(num):
```
  

Reverse the ordering of digits in the given input and return the result. Here, we are treating the input not like a single large number, but like a “string” of consecutive digits. This type of interpretation is often used when storing text in computers: a string of letters are stored in a big number, where different regions of that number store different letters.

### Examples:

``` 
>>>reverse_digits(2)
2
>>>reverse_digits(1234)
4321
>>>reverse_digits(90000)
9
```