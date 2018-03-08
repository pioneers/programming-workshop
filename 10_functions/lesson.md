# Intro to Programming Workshop

## Lesson 10 - Functions

This section was adapted with modifications from [Think Python](http://greenteapress.com/thinkpython2) by [Allen B. Downey](http://greenteapress.com/wp/) ([CC BY 3.0](https://creativecommons.org/licenses/by-nc/3.0/)).

In the context of programming, a function is a named sequence of statements that performs a computation. When you define a function, you specify the name and the sequence of statements. Later, you can “call” the function by name.

###  Function calls

We have already seen one example of a function call:

	> type(42)
	<class 'int'>

The name of the function is type. The expression in parentheses is called the argument of the function. The result, for this function, is the type of the argument.

It is common to say that a function “takes” an argument and “returns” a result. The result is also called the return value.

###  Composition

So far, we have looked at the elements of a program—variables, expressions, and statements—in isolation, without talking about how to combine them.

One of the most useful features of programming languages is their ability to take small building blocks and compose them. For example, the argument of a function can be any kind of expression, including arithmetic operators. `print` which we have been using is another example of a function.

	x = type(degrees / 360.0 * 2 * pi)

Almost anywhere you can put a value, you can put an arbitrary expression, with one exception: the left side of an assignment statement has to be a variable name. Any other expression on the left side is a syntax error (we will see exceptions to this rule later).

	> minutes = hours * 60                 # right
	> hours * 60 = minutes                 # wrong!
	SyntaxError: can't assign to operator

### Adding new functions

So far, we have only been using the functions that come with Python, but it is also possible to add new functions. A function definition specifies the name of a new function and the sequence of statements that run when the function is called.

Here is an example:

	def print_lyrics():
	    print("I'm a lumberjack, and I'm okay.")
	    print("I sleep all night and I work all day.")

`def` is a keyword that indicates that this is a function definition. The name of the function is `print_lyrics`. The rules for function names are the same as for variable names: letters, numbers and underscore are legal, but the first character can’t be a number. You should avoid having a variable and a function with the same name.

The empty parentheses after the name indicate that this function doesn’t take any arguments.

The first line of the function definition is called the header; the rest is called the body. The header has to end with a colon and the body has to be indented. By convention, indentation is always four spaces or a tab. The body can contain any number of statements.

The syntax for calling the new function is the same as for built-in functions:

	> print_lyrics()
	I'm a lumberjack, and I'm okay.
	I sleep all night and I work all day.

Once you have defined a function, you can use it inside another function. For example, to repeat the previous refrain, we could write a function called `repeat_lyrics`:

	def repeat_lyrics():
	    print_lyrics()
	    print_lyrics()

And then call `repeat_lyrics`:

	> repeat_lyrics()
	I'm a lumberjack, and I'm okay.
	I sleep all night and I work all day.
	I'm a lumberjack, and I'm okay.
	I sleep all night and I work all day.

### Definitions and uses

Pulling together the code fragments from the previous section, the whole program looks like this:

	def print_lyrics():
	    print("I'm a lumberjack, and I'm okay.")
	    print("I sleep all night and I work all day.")

	def repeat_lyrics():
	    print_lyrics()
	    print_lyrics()

This program contains two function definitions: `print_lyrics` and `repeat_lyrics`. Function definitions get executed just like other statements, but the effect is to create function objects. The statements inside the function do not run until the function is called, and the function definition generates no output.

As you might expect, you have to create a function before you can run it. In other words, the function definition has to run before the function gets called.

###  Flow of execution

To ensure that a function is defined before its first use, you have to know the order statements run in, which is called the flow of execution.

Execution always begins at the first statement of the program. Statements are run one at a time, in order from top to bottom.

Function definitions do not alter the flow of execution of the program, but remember that statements inside the function don’t run until the function is called.

A function call is like a detour in the flow of execution. Instead of going to the next statement, the flow jumps to the body of the function, runs the statements there, and then comes back to pick up where it left off.

That sounds simple enough, until you remember that one function can call another. While in the middle of one function, the program might have to run the statements in another function. Then, while running that new function, the program might have to run yet another function!

Fortunately, Python is good at keeping track of where it is, so each time a function completes, the program picks up where it left off in the function that called it. When it gets to the end of the program, it terminates.

In summary, when you read a program, you don’t always want to read from top to bottom. Sometimes it makes more sense if you follow the flow of execution.

### Parameters and arguments

Some of the functions we have seen require arguments. For example, when you call math.sin you pass a number as an argument. Some functions take more than one argument: math.pow takes two, the base and the exponent.

Inside the function, the arguments are assigned to variables called parameters. Here is a definition for a function that takes an argument:

	def print_twice(bruce):
	    print(bruce)
	    print(bruce)

This function assigns the argument to a parameter named `bruce`. When the function is called, it prints the value of the parameter (whatever it is) twice.

This function works with any value that can be printed.

	> print_twice('Spam')
	Spam
	Spam
	> print_twice(42)
	42
	42
	> print_twice(pi)
	3.14159265359
	3.14159265359

The same rules of composition that apply to built-in functions also apply to programmer-defined functions, so we can use any kind of expression as an argument for `print_twice`:

	> print_twice('Spam '*4)
	Spam Spam Spam Spam
	Spam Spam Spam Spam
	> print_twice(1 - 2)
	-1.0
	-1.0

The argument is evaluated before the function is called, so in the examples the expressions `'Spam '*4` and `1 - 2` are only evaluated once.

You can also use a variable as an argument:

	> michael = 'Eric, the half a bee.'
	> print_twice(michael)
	Eric, the half a bee.
	Eric, the half a bee.

The name of the variable we pass as an argument (`michael`) has nothing to do with the name of the parameter (`bruce`). It doesn’t matter what the value was called back home (in the caller); here in `print_twice`, we call everybody `bruce`.

### Variables and parameters are local

When you create a variable inside a function, it is local, which means that it only exists inside the function. For example:

	def cat_twice(part1, part2):
	    cat = part1 + part2
	    print_twice(cat)

This function takes two arguments, concatenates them, and prints the result twice. Here is an example that uses it:

	> line1 = 'Bing tiddle '
	> line2 = 'tiddle bang.'
	> cat_twice(line1, line2)
	Bing tiddle tiddle bang.
	Bing tiddle tiddle bang.

When `cat_twice` terminates, the variable cat is destroyed. If we try to print it, we get an exception:

	> print(cat)
	NameError: name 'cat' is not defined

Parameters are also local. For example, outside `print_twice`, there is no such thing as `bruce`.

### Fruitful functions and void functions

Some of the functions return results; for lack of a better name, I call them fruitful functions. Other functions, like `print_twice`, perform an action but don’t return a value. They are called void functions.

When you call a fruitful function, you almost always want to do something with the result; for example, you might assign it to a variable or use it as part of an expression:

	def square(number):
		return number * number

	x = sqaure(22)
	length = (square(5) + 1) / 2

When you call a function in interactive mode, Python displays the result:

	> square(4)
	16

But in a script, if you call a fruitful function all by itself, the return value is lost forever!

	square(4)

This script computes the square of 4, but since it doesn’t store or display the result, it is not very useful.

Void functions might display something on the screen or have some other effect, but they don’t have a return value. If you assign the result to a variable, you get a special value called None.

	> result = print_twice('Bing')
	Bing
	Bing
	> print(result)
	None

The value None is not the same as the string 'None'. It is a special value that has its own type:

	> type(None)
	<class 'NoneType'>

The functions we have written so far are all void. We will start writing fruitful functions in a few chapters.

###  Why functions?

It may not be clear why it is worth the trouble to divide a program into functions. There are several reasons:

Creating a new function gives you an opportunity to name a group of statements, which makes your program easier to read and debug.
Functions can make a program smaller by eliminating repetitive code. Later, if you make a change, you only have to make it in one place.
Dividing a long program into functions allows you to debug the parts one at a time and then assemble them into a working whole.
Well-designed functions are often useful for many programs. Once you write and debug one, you can reuse it.
