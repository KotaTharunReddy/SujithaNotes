# Python Exceptions

# In Python, an exception is an event that disrupts the normal flow of a program. 
# When an exception occurs, the program terminates if the exception is not handled. 
# However, Python provides a structured way to handle these exceptions, preventing your program from crashing unexpectedly.

# Types of Exception

# Python has a wide range of built-in exceptions, each designed to handle a specific type of error. 
# Understanding these exceptions is crucial for effective error handling in your code.

# Let’s have a look for some common exceptions occur at the time of programming:

# Common exceptions	    Explaination
# 
# SyntaxError	        A SyntaxError is raised when there is a syntax mistake in your code. This can include incorrect indentation, missing colons, or invalid characters.
# IndentationError	    IndentationError occurs when the indentation of your code is not consistent. Python relies on proper indentation to define code blocks.
# NameError	            NameError is raised when a local or global name is not found. It usually indicates a typo or referencing a variable that doesn’t exist. Like NullPointerException is not a built-in exception in Python. It is commonly found in languages like Java, but in Python, it is known as a NameError.
# TypeError	            A TypeError occurs when an operation or function is applied to an object of an inappropriate type. For example, trying to add a string and an integer.
# ValueError	        ValueError is raised when a function receives an argument of the correct type but an inappropriate value. For instance, trying to convert a non-numeric string to an integer.


# Exception Handling
# try….except Block: To handle exceptions, Python provides the try….except block. It allows you to catch and handle exceptions gracefully, preventing your program from crashing.
# Handling Multiple exceptions: You can use multiple except blocks to handle different types of exceptions, providing a customized response for each.
# The finally Block: The finally block is used to execute code regardless of whether an exception was raised or not. It is often used for cleanup operations.

# Some Important Statements for Exception:
# The raise statement is used to raise an exception in Python. It allows the programmer to explicitly raise an exception when a specific condition is met. If an exception is raised within a try block but not caught by any except block, the program crashes and displays an error message. This is because the exception is not handled, causing the program to terminate abruptly.
# The assert statement is used to raise an exception when a specific condition is met. It is commonly used for debugging purposes to check if a certain condition is true, and if not, raise an AssertionError.

def example_function(x, y):
    try:
        # Attempting division operation
        result = x / y
        print("Result:", result)
        
        # Accessing an undefined variable
        # print(undefined_variable)
        
    except ZeroDivisionError as e:
        # Handling ZeroDivisionError
        print("ZeroDivisionError:", e)
        
    except NameError as e:
        # Handling NameError
        print("NameError:", e)
        
    except Exception as e:
        # Handling any other exceptions
        print("Other Exception:", e)
        
    finally:
        # Finally block executes regardless of whether an exception occurred
        print("Finally block executed")

# Calling the function with different arguments to trigger exceptions
example_function(10, 0)
example_function(10, 'a')
































































