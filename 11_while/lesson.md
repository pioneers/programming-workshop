# Intro to Programming Workshop

This section was adapted with modifications from [Think Python](http://greenteapress.com/thinkpython2) by [Allen B. Downey](http://greenteapress.com/wp/) ([CC BY 3.0](https://creativecommons.org/licenses/by-nc/3.0/)).

## Lesson - While Loops

Computers are often used to automate repetitive tasks. Repeating identical or similar tasks without making errors is something that computers do well and people do poorly. In a computer program, repetition is also called iteration.

One way we can do this in Python is with the `while` statement. Here is a function that counts down using a while statement:

def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')

You can almost read the while statement as if it were English. It means, “While n is greater than 0, display the value of n and then decrement n. When you get to 0, display the word Blastoff!”

More formally, here is the flow of execution for a while statement:

Determine whether the condition is `True` or `False`.
If `False`, exit the while statement and continue execution at the next statement.
If the condition is `True`, run the body and then go back to step 1.

This type of flow is called a loop because the third step loops back around to the top.

The body of the loop should change the value of one or more variables so that the condition becomes false eventually and the loop terminates. Otherwise the loop will repeat forever, which is called an infinite loop. An endless source of amusement for computer scientists is the observation that the directions on shampoo, “Lather, rinse, repeat”, are an infinite loop.

In the case of countdown, we can prove that the loop terminates: if n is zero or negative, the loop never runs. Otherwise, n gets smaller each time through the loop, so eventually we have to get to 0.

## Practice

Let's get some practice! Let's make a function that will count up to a number from 0. We've given you some code to get started.

Remember to consider:

* What's the condition we want to check everytime we run the contents of the loop?
* The contents of the loop need to be indented with a tab
* How will we change the varaibles so that the condition eventually becomes false?

Here's what calling `countup` should do:

	> countup(5)
	0
	1
	2
	3
	4
	5
	Blastoff!

How might you change your function if you wanted to create another function that counted up in increments of 3? Or squared itself everytime?

