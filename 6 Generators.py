# Python Generators

# Generators are a type of iterable, like lists and tuples, but with a significant difference. While lists store all their values in memory, generators produce values on the fly, saving memory resources. 
# In essence, generators are lazy iterators that generate values one at a time, making them ideal for processing large datasets efficiently.

# Creating a Generator Function
# To create a generator, you define a function with the yield keyword.

# Example:
def simple_generator():
    yield 1
    yield 2
    yield 3

# Code for Simple Generator Function : 

def simple_generator():
    yield 1
    yield 2
    yield 3

# Using the generator
gen = simple_generator()
for value in gen:
    print(value)

# Output : 
# 1
# 2
# 3

# Use Cases for Generators

# Generators are incredibly useful in scenarios where memory efficiency is crucial. 
# Some common use cases include reading large files, generating infinite sequences, and processing data streams.

# Advantages of Generators

# Generators have several advantages:

# They save memory by producing values on-the-fly.
# They can represent infinite sequences.
# They allow for more readable and efficient code.
# They support pipelining and chaining operations.
    
# Let’s see an example of an infinite generator that generates even numbers

def infinite_even_generator():
    n = 0
    while True:
        yield n
        n += 2

# Using the infinite generator
gen = infinite_even_generator()
for _ in range(5):
    print(next(gen))

# Output : 
# 0
# 2
# 4
# 6
# 8
    
# Generators in Python provide a powerful mechanism for efficient and memory-friendly data processing. 
# By generating values lazily, they allow you to work with large datasets without straining your system’s resources. 
# Embrace the power of generators to write more efficient and responsive Python code.














































