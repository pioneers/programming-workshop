# Intro to Programming Workshop

## Lesson 1 - Print statements

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
    
we can fix our `SyntaxError` by keeping our print statements on separate lines.

### What else?

What else can we print? Try printing a number:

    print(314)

See what else you can print - your name, negative numbers?

When you're done experimenting move on to the next lesson.
