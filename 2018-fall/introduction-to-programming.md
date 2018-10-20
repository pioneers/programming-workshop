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
* Writing instructions for computers called **code**.
* Computers follow instructions *exactly*.
* Most errors caused by giving wrong or unclear instructions.
* Code is written in a language like Python.

# Hello World!
Programs are written in lines.

First program in Python:
```python
>>> # A line with a pound sign is a comment.
... # Comments tell other people what your code
... # does, but the computer knows to ignore
... # everything after the pound sign.
... print('Hello world!')
```

# Expressions
Doing math quickly:
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
>>> (1 + 1)*3  # Grouping expressions
6
```

# Expressions
Comparing numbers:
```python
>>> 1 < 1  # Is one less than one?
False
>>> 1 == 1  # Is one equal to one?
True
>>> 1 <= 2  # Is one less than or equal to one?
True
>>> 1 != 3  # Is one not equal to three?
True
```

# Variables
* Variables store values that will be used later using *names*.
* Assign variables with:
    1. Variable name on the left
    2. Equals sign
    3. Value on the right

```python
>>> x = 5
>>> x + 1  # Substitute current value of x here
6
>>> x*x + 3*x  # Simplifies to 2*2 + 3*2
10
```

# Variables
What happens if we use a name we haven't used before?
```
>>> y + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
```

* The computer is not sure what `y` is.
* The computer raises an error and stops.

# Variables
* Variables can be reassigned.
* Only the most recent assignment counts.
* The old value is destroyed.
```python
>>> x = 2
>>> x = 3
>>> x + 1
4
>>> x = x + 1  # Update x using its current value
>>> x
5
```

# Variables
* Variables can also be pieces of text called **strings**.
* Strings are surrounded by single or double quotation marks.
```python
>>> first_name = 'James'
>>> print(first_name)
James
>>> full_name = first_name + ' Hulett'
>>> print(full_name)
James Hulett
```

# Functions
A function is a block of reusable code that does a particular task.
```python
>>> def say_hello():
...     print('Hello!')
```

The code stays dormant until we call it.
```python
>>> say_hello()
Hello!
```

# Functions
Functions can accept **arguments**, which are temporary variables only available in the function.
```python
>>> def greet(name):
...     print('Hello ' + name)
>>> greet('James')  # Assigns "James" to name
Hello James
>>> greet('Julie')  # Easy to greet many people
Hello Julie
```

# Functions
Functions can also **return** values using the `return` keyword.
```python
>>> def create_milkshake(ingredient):
...     return ingredient + ' milkshake'
>>> milkshake1 = create_milkshake('Strawberry')
>>> milkshake2 = create_milkshake('Chocolate')
>>> print(milkshake1)
Strawberry milkshake
>>> print(milkshake2)
Chocolate milkshake
```

# Conditionals
Run blocks of code only when a certain condition is met.
```python
>>> password = 'potato'
>>> guess = 'not potato'
>>> if guess == password:
...     print('Logged in!')
... else:
...     print('Incorrect!')
Incorrect!
```

# Loops
* Loops are used to repeatedly run a segment of code.
* Avoids writing many common instructions over and over.
```python
>>> print(0)
0
>>> print(1)
1
>>> print(2)
2
```

# Loops
* Use the `while` keyword to test a condition like an `if`-statement.
    1. If the condition is true, run the block and then test the condition again.
    2. Otherwise, exit the loop.

```python
>>> counter = 0
>>> limit = 3
>>> while counter < limit:
...     print(counter)
...     counter = counter + 1
0
1
2
```
