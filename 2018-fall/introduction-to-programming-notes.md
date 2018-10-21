---
output:
  html_document: default
  pdf_document: default
---
# Introduction to Programming

Pioneers in Engineering

Fall Competition

October 20, 2018

# What *is* programming?
* Writing instructions for computers

# Hello World!

```python
>>> print('Hello world!')
```

# Expressions

Doing math with Python:
```python
>>> 1 + 1  # Addition
2
>>> 5 - 1  # Subtraction
4
>>> 2 * 3  # Multiplication
6
>>> 1 / 3  # Division
0.3333333333333333
>>> -1 - 2 # Negative numbers
-3
```

# Expressions

Computers work great as a calculator and are very good at following instructions. However, they will do exactly as the instructions says. Point being, computers do not do what you intend them to do, they do as they are told to do. This fact can be very frustrating so do not be discouraged if your code does not work at first. We are all learning and continue to learn.

# Variables

### Main Idea

A variable can be used to store information or values that will be used later.

### Intuition

Much like people can be referenced by names, variables too can be referenced. Commonly in math, we will name a variable $x$. This variable $x$ can take any value that we want. We can have our variable be called anything (say "Mark" for example). For now though, lets stick with variables like in math.

### Intuitive Example

**a)** $x = 7$ is a perfectly valid assignment. If later we say that we want $2*x$ we know that we actually want the product $2*7=14$.

**b)** We can even make name more complicated values. Take $y = x^2 +7*x$. We can represent a whole variety of things by naming our variables and using them later.

### In Programming

We don't have to do the assignment $x=7$. We can make $x$ whatever number we want such as $x=4$. However, in programming we are even less restricted.
```python
>>> x = 7
>>> y = "howdy"
>>> Mark = (1,2,3,4)
>>> Julie = "Lame"
>>> Jesse = "Cool"
```
If we at a later time we want to reference a value, we can simply reference it.

```python
>>> x = 7
>>> y = "howdy"
# code code code
>>> 2*x
14
>>> print(y)
"howdy"
```

### Renaming
We can give new values to existing variables if we like. This can be confusing, but it can very powerful. As we know in math $x=7$ is not the only possibly assignment. I can plug in any value I want. Just be careful to look at the most recent assigment to know what the value of $x$ is!

```python
>>> x=7
>>> x=10
>>> 2*x
20
```

The above is equivalant to saying:

- "Hey, $x$! Your value is now 7."

- "Hey, $x$! Your value is now 10."

- "Hey, computer! What is 2 times $x$?"

We can also update a variable based upon its current value.

```python
>>> x=7
>>> x=5*x
>>> 2*x
70
```

The above is equivalant to saying:

- "Hey, $x$! Your value is now 7."

- "Hey, $x$! Your value is now 2 times your current value."

- "Hey, computer! What is 2 times $x$?"

# Functions

### Main Idea

A function can be used to do a task. A function takes in information to use in performing its task.

### Intuition

Sometimes we want to do a similar task over and over again. Rather than writing the instructions down for all possible cases, we can write the instructions for a general case and work from there.

### Intuitive Example

Say we want to make a milkshake. We could give instructions for how to make a chocolate milkshake, a vanialla milkshake, a strawberry banana soy milkshake, and so on. Alternatively, we could give instructions for a general milkshake and let the user fill out the specific types of ingredients. Point being we can generalize our instructions to:

1. Ingredients:

- ice

- main flavor

- secondary flavor (optional)

- dairy or dairy imitation product

2. Mix ingredients in blender.
3. Serve in a cup

### In Programming

Let us take our intuitive example and translate it into code. First, we will determine all of the corresponding parts.

1. The ingredients will become our _**parameters**_. These are the objects or value our function will take in.

2. The second step of mixing the ingredients will be our _**body**_. Most of our operations and steps will take place here.

3. Serving in the cup is in essence what our function will _**return**_. We push out the finished product at the end.

Thus our code will look something like this:

```python
def yummy_in_my_tummy(ice, main_flavor, secondary_flavor = None, liquid)
  # check if there is a second ingredient and use if there is one
  # mix the ingredients
  return milkshake
```

Note that the parameter secondary_flavor is set to None. We can preset our parameters if we do not want to require a user to input a value for them.

# Loops

### Main Idea

Loops are used to repeadetly perform an action or run a segment of code.

### Intuition

What if we want to do a task over and over again? A cookbook will not give the instructions of blending 6 or so times in a row. As you can imagine it would be silly to see:

If not done then keep blending. If not done, then keep blending. If not done then keep blending. If not done, then keep blending. If not done then keep blending. If not done, then keep blending. If not done then keep blending. If not done, then keep blending. If not done then keep blending. If not done, then keep blending.

### Intuitive Example

Allow us to write some instructions for our milkshake again. Realistically, a cookbook would say:

While the smoothie contains chunks you should keep blending.

### In Programming

A very powerful loop is the _**while**_ loop. Converting our intuitive example to code gives us something like this:

```python
chunky = true
while chunky:
  # mix the ingredients
  # update chunky to be true or false
```

# Conditionals

### Main Idea

If statements are used to run code chunks only when appropriate.

### Intuition

What if we want to do a task only when it makes sense to do so? Putting a secondary favlor into our milkshake doesn't make sense if we don't have a second flavor. 

### Intuitive Example

> If we have a secondary flavor

> then put the secondary flavor into the milkshake.

Note that we only perform the second line when the if statement is true.

Alternatively, we may say:

> If the secondary flavor is not nothing

> then put the secondary flavor into the milkshake.

Note again that we only perform the second line when the if statement is true.

### In Programming

We will tranlsate the alternative statement from our intuitive example into code.

```python
if secondary_flavor != None:
  # add the secondary flavor to the milkshake
```

# All Together Now

Combing all the topics we have seen allows us to make instructions for our milkshake.

In English we have:

1. Ingredients:

  - ice
  
  - main flavor
  
  - secondary flavor (optional)
  
  - dairy or dairy imitation product
  
2. Mix ingredients in blender.

3. Serve in a cup

In code we have:

```python
def yummy_in_my_tummy(ice, main_flavor, secondary_flavor = None, liquid)
  milkshake = None
  if secondary_flavor != None:
    # add the secondary flavor to the milkshake
  chunky = True
  while chunky:
    # mix the ingredients
    # update chunky to be true or false
  return milkshake
```