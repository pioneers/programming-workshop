# Intro to Programming Workshop

## Lesson 9 - Integer Traversal

We're going to take a look at how we might be able to use all the things we've learned so far to play with numbers.

We're given a number in the variable `num`. We want to print each digit in `num` on a new line, starting with the ones place, then the tens place, etc.

Here's a few examples:

	> line_print(3145)
	5
	4
	1
	3
	
	> line_print(32)
	2
	3

	> line_print(5)
	5

We've given you some template code to get started.

	def line_print(num):
		pass

How can we go about this? Let's break it down.

### The ones place

First, how can we identify what the last digit in a number is? You may recall from Lesson 6 that we can use the modulus operator, `%` to find the remainder when one number is divided by another. 

A refresher on how to use the modulus operator

	> 7 % 3
	4

How might we be able to use this to identify the last digit in a number? We can do this activity in a helper function, or a small function that helps us achieve a larger task.

	def find_last_digit(number):
		# Your code below
		pass
		# Your code above

	number = 3145
	last_digit = find_last_digit(number)

Example behavior:

	> find_last_digit(3145)
	5
	> find_last_digit(38)
	8
	> find_last_digit(10)
	0

### Finding the next digit

Now, how can we find the tens-place digit?

Note that now that we've found the ones-place digit, we no longer need to keep it around necessarily. Is there a way we can reuse our `find_last_digit` function to help us identify the tens-place digit?

	> number = 3145
	> ones_place = find_last_digit(number)
	> tens_place = find_last_digit(some new value based on number?)
		
Hint: the `int` function can be used to round down any `float` to the next lowest integer

	> int(3.14)
	3
	> int(9.99)
	9
	> int(4.0)
	4

### Looper

Now that we've found a repeatable process, this seems like a great candidate for a while loop. we can add what we have as the contents of the while loop. 

	def find_last_digit(number):
		# Your code below
		pass
		# Your code above

	def line_print(number):
		# Replace condition
		while(condition):
			print(find_last_digit(number))

			# Give number a new value,
			# using the process we found in the last section


What is the condition when we are done? When do we want to stop printing the last digit of the value stored in `number`?

Let's test it out! We can run our test cases:

	> line_print(3145)
	5
	4
	1
	3
	
	> line_print(32)
	2
	3

	> line_print(5)
	5

Great! We've now fully implemented our `line_print` function.

### How can we use this?

We're now going to try to implement a new function that returns a new number with the reverse order of digits in a number. This function has some importance in this year's game. That's all we've been told we're allowed to say before Game Day. 

	> reverse_digits(2)
	2
	reverse_digits(1234)
	4321
	reverse_digitss(90000)
	9

How might be able to build off of `line_print` to implement `reverse_digits`?

Hints:
1. It will be useful to have a variable to hold our answer that we are gradually making.
2. How can we gradually make progress towards our final answer?
3. What actions will get us a little closer each time?

Some code to get you started:

	def reverse_digits(number):
		# Your code below
		pass
		# Your code above
