# Intro to Programming Workshop

## Lesson 6 - Advanced Operations

We talked about math operations like `+`, `-`, `*`, and `/` in Lesson 3. We will now introduce two more.

### Exponent

We can take the exponent of a number using `**`

    > 3**2
    9.0

The code above reads as `3` to the power of `2` which equals `9.0`.

A special note, the exponent returns a `float`, even if both inputs are `int`s.

Try it out!

### Remainder

The modulus operator, `%`, divides two numbers and returns the remainder

    > 7 % 3
    1

The code above says that the remainder of `7` divided by `3` is `1`.

Why would we ever need to know a remainder?
Finding the remainder can be very useful for determining if a number is even or odd. Odd numbers always have a remainder of 1 when divided by 2. Even numbers always have a remainder of 0 when divided by 2.

    > 23 % 2
    1

How might we be able to tell what the last digit of a number is? We'll come back to this topic in later lessons.
