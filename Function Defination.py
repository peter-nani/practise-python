#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#while and else: The else part is executed if the condition in the while loop evaluates to False.
'''FUNCTION DOCUMENT:

def function_name(parameters):
	"""docstring"""
	statement(s)

Above shown is a function definition that consists of the following components.

1.Keyword def that marks the start of the function header.
2.A function name to uniquely identify the function. Function naming follows the same rules of writing identifiers in Python.
3.Parameters (arguments) through which we pass values to a function. They are optional.
4.A colon (:) to mark the end of the function header.
5.Optional documentation string (docstring) to describe what the function does.
6.One or more valid python statements that make up the function body.
7.Statements must have the same indentation level (usually 4 spaces).
8.An optional return statement to return a value from the function.'''

# 2 keyword arguments
#greet(name = "Bruce",msg = "How do you do?")

# 2 keyword arguments (out of order)
#greet(msg = "How do you do?",name = "Bruce")

#1 positional, 1 keyword argument
#greet("Bruce", msg = "How do you do?")