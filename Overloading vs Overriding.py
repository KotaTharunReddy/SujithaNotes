# Method Overloading:

# Method overloading refers to defining multiple methods in a class with the same name but with different parameters or argument lists. 
# In Python, method overloading is achieved through default parameter values or variable-length argument lists.

# Example:

class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

math_obj = MathOperations()
print(math_obj.add(2, 3))       # Output: TypeError: add() missing 1 required positional argument: 'c'
print(math_obj.add(2, 3, 4))    # Output: 9

# Method Overriding:

# Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. 
# This allows the subclass to change or extend the behavior of the inherited method.

# Example:
class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

animal = Animal()
animal.make_sound()    # Output: Generic animal sound

dog = Dog()
dog.make_sound()       # Output: Woof

cat = Cat()
cat.make_sound()       # Output: Meow

# In the example for method overriding, both the Dog and Cat classes have overridden the make_sound() method 
# inherited from the Animal class to provide specific sounds for dogs and cats, respectively.

































































