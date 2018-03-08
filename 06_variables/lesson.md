# Intro to Programming Workshop

## Lesson 5 - Variables

This section was adapted with modifications from [Think Python](http://greenteapress.com/thinkpython2) by [Allen B. Downey](http://greenteapress.com/wp/) ([CC BY 2.0](https://creativecommons.org/licenses/by/2.0/)).

One of the most powerful features of a programming language is the ability to manipulate variables. A variable is a name that refers to a value.

### Assignment statements

An assignment statement creates a new variable and gives it a value:

	message = 'And now for something completely different'
	n = 17
	pi = 3.141592653589793

This example makes three assignments. The first assigns a string to a new variable named `message`; the second gives the integer 17 to `n`; the third assigns the (approximate) value of π to `pi`.

### Variable names

Programmers generally choose names for their variables that are meaningful—they document what the variable is used for.

Variable names can be as long as you like. They can contain both letters and numbers, but they can’t begin with a number. We will usually use only lower case for variables names.

The underscore character, `_`, can appear in a name. It is often used in names with multiple words, such as `your_name` or `airspeed_of_unladen_swallow`.

If you give a variable an illegal name, you get a syntax error:

	> 76trombones = 'big parade'
	SyntaxError: invalid syntax
	> more@ = 1000000
	SyntaxError: invalid syntax

`76trombones` is illegal because it begins with a number. `more@` is illegal because it contains an illegal character, @.

### Why would I use variables?

Let's go through a case where you might want to use a variable: keeping track of how many points you have during the middle of a game.

	# Create a new variable 
	number_of_points = 10

The variable `number_of_points` will keep track of our current number of points in the match. Let's start a new game.

	# Start a new game and reset our points to 0
	number_of_points = 0

We're doing great while playing and score a goal! We get five more points

	# Score a goal and get five more points
	number_of_points = nubmer_of_points + 5

Wait, how can `number_of_points` be equal to itself plus five? With assignment statements, Python will:

1. Determine the value of whatever is on the right side of `=`
2. Assign that value to the variable on the left

Python first determines the value of `number_of_points + 5`. We assigned `number_of_points` a value of `0` earlier, so `number_of_points + 5` is 5. Thus, we assign a value of 5 to `number_of_points`.

Let's check that we're correct with by printing the value of `number_of_points`.

	# Check our score
	print("After scoring, we have", number_of_points, "points")
