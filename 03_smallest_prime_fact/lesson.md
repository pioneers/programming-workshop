# Smallest Prime Factor
```
def smallest_prime_fact(num):
```


Find the smallest prime factor of the input. A prime factor is defined as a prime number that divides our input with no remainder. All prime factors of a given input satisfy the following properties:

-   Integer greater than 1.
    
-   Divisible evenly by only 1 and itself.
    
-   Divides the given input exactly with no remainder.
    

  

A number can have multiple prime factors. Your task is to find the smallest one!

  

Special case: If we give you an input that has no prime factors, just return the unmodified input.

### Examples:

```
>>> smallest_prime_fact(2)
2
>>> smallest_prime_fact(3)
3
>>> smallest_prime_fact(59*53)
53
>>> smallest_prime_fact(2557)
2557
>>> smallest_prime_fact(1251)
3
```
