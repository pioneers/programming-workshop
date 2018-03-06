# Intro to Programming Workshop

## Lesson 1 - Print statements

Welcome to the Introduction to Programming Workshop. 

By the end of this workshop, you should understand how to program with Python. Unlike previous years, we will not be covering how to program your robot. Rather, we will concentrate our time on how to use Python. Much of our workshop will be applicable to programming your robot, but everything you learn here will strengthen your understanding of Python.

Let's get started!

### Print statements

Print statements allow us to display something to the screen.

Hit `run` to run the program we've written in the top left box. You can then see the result in the bottom left box: `Hello World!`

What else can we print? On a new line, add another print statement

    print("Hello World!")
    print("Pioneers in Engineering")

After hitting run, we can see that both `Hello World!` and `Pioneers in Engineering` will appear. 


### Spacing
Notice that we had to put the second print statement on a new line. If we try putting both print statements on a single line:

    print("Hello World!") print("Pioneers in Engineering")
    
We'll get a `SyntaxError` on `line 1`.

    Traceback (most recent call last):
    File "python", line 1
      print("Hello World") print("Pioneers")
                             ^
    SyntaxError: invalid syntax
    
### What else?

What else can we print? Try printing a number:

    print(314)

See what else you can print - your name, negative numbers?

When you're done experimenting move on to the next lesson.
