# Intro to Programming Workshop

## Lesson 7 - Booleans and Conditionals

Up until now our code has always run in the same order. However, we often want our program to perform different actions depending on what else is happening in the program. We can utilize **booleans** and **conditionals** in order to give our program to choose among outcomes.

### Booleans

We will start with booleans. Boolean is another type, similar to string or int. Booleans, however, only have two possible values: `True` or `False`. 

Another key term we will introduce is **comparator**. We have six comparators in python:
1. `<`: Less Than
2. `>`: Greater Than
3. `<=`: Less Than or Equal To
4. `>=`: Greater Than or Equal To
5. `==`: Equal To
6. `!=`: Not Equal To

We use each different type of comparator with two values like `4 > 2` or `1 == 1`, and the comparison returns a boolean to us. Looking at the first comparison (`4 > 2`) we say "Is 4 greater than 2? False". Therefore, this statement is equivalent to the value of False. Look at lines 1-3 of the example and try to determine what boolean value (True or False) each expression is equivalent to.

### Conditionals

We will now user our knowledge of booleans to help our code make different decisions! We will write what we call **conditional** statements. Take a look at the following block of code:

```
x = True
if x:
    print("Go!")
else:
    print("Bears!")
```

Notice that variables not only can store string and integers, but also can store booleans! In this code block, we can see that we have two new python words: `if` and `else`. What this says is "If `x` is True, then run the code indented under the if block, ELSE run the code indented unter the else block. The value of `x` (True or False) actually affects what parts of the code are run! 

Now lets put it all together. Look at the code starting at line 5. Change the values of `x` and `y` so that the phrase "Pioneers in Engineering" is printed out. (Hint: The statement after the word `if` just needs to be a boolean value, either `True`, a variable, or some comparison)
