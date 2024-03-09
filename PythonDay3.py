# Contents
# 1. INHERITENCE
# 2. ENCAPSULATION
# 3. ABSTRACTION
# 4. POLYMORPHISM

# Activity: Ravi recently started his job as an Employee, his salary is 
# Rs 5000 a month, his job is to approveLoans.

# Class : Employee
# Object : Ravi
# Attribute : Salary=5000
# Method: ApproveLoan

class Employee:                     # class here
    salary = 5000                   # Property here
    def approveLoan(self):          # method here
        print ("I Approve Loans")
ravi = Employee()                   # Object here
print('Ravi\'s Salary', ravi.salary)
ravi.approveLoan()
# self is reference to object ravi 
# python does this automatically

# In Python, 'instance' and 'object' are often used interchangeably to refer to 
# a specific occurrence of a class. An 'object' is a concrete entity created based on 
# the blueprint provided by a class. An 'instance' specifically refers to a 
# unique occurrence of that object during program execution.

class Student:
    def sample(self):
        self.gift="bose revolve 2"
        fakeGift="sasta iphone"

ravi = Student()
ravi.sample()

print(ravi.gift)
print(ravi.fakeGift) # this is valid variable but local as 
                     # it is not referenced with object
                     # that means not referenced with self

# Who is self?
# self is the object who is calling the function
# i.e Ravi.

# if u write self.var it gets attached with ravi
# if u write just var it is valid but local variable
# doesn't gets attached to object i.e ravi

# when a new baby gets delivered he will have copy 
# of everything from mother like head hair nails etc

# so when we create object of class then every copy 
# of variable and function will be created for each and 
# every object

# here is the example of above application

class Student:
    score=0

shubham=Student()
aniket=Student()
rajat=Student()

shubham.score=10
aniket.score=20
rajat.score=shubham.score + aniket.score

print('shubham : ', shubham.score) # shubham :  10
print('aniket: ', aniket.score)    # aniket:  20
print('rajat: ', rajat.score)      # rajat:  30


# object to object assignment

himanshu=rajat
print(himanshu.score)   # 30
# we are giving reference of rajat to himanshu
# this means himanshu share the members of rajat i.e, score

# in which case himanshu create separate copy of variable
# i.e, calling the constructor for himanshu
himanshu=Student.score

# this is the difference between 
# object = object
# object = constructor

print(id(aniket))       # 1655225279424
print(id(rajat))        # 1655225279520
print(id(himanshu))     # 1655225279520

# id's of rajat and himanshu are same because himanshu
# is taking reference from rajat
# id's are not like addresses they are identifiers


#identifying diff b/w static and instance variable

class Guest:
    channel = "Discover"
    def getChannel(self):
        print("I am watching ", Guest.channel)

    def changeChannel(self):
        Guest.channel = "National Geographic"

kartik=Guest()
priyanshu=Guest()
haider=Guest()

kartik.getChannel()
priyanshu.getChannel()
haider.getChannel()

priyanshu.changeChannel()

kartik.getChannel()
priyanshu.getChannel()
haider.getChannel()



# Inheritance
# Inheritance allows us to acquire the properties
# and functions of base class in derived class.

# Advantages of Inheritance
#   1. Code Reusability
#   2. Memory Optimizations

class Father:
    def foodHabit(self):
        print('I like Salty')

class Son (Father):
    pass # This keyword is used to keep coding blocks Empty

ravi = Son()

print(ravi.foodHabit())

# Encapsulation
# Encapsulation be defined as a practice of controling
# the access or Exposition of Member variables & Functions
# using Access Modifiers.

# we provide access to the variables & Functions
# using getters and getters methods

class abc:
    __privateVar=0 # prefixing the variable with double underscore to make it private variable
    publicVar=0    # underscore it is private or else public


# this can be well explained using java
# sir took java example
# refer to Program2.java in WileyEdge folder on desktop
    
# // therefore encapsulation helps control or restrict access
# // to variable or functions using access specifiers

# // when the variable is marked as private
# // the variable is encapsulated in its own class.

# // when the variable is marked as protected 
# // the variable is encapsulated in its own class
# // and in derived class

# //when the variable is marked as default(no acceess modifier)
# // then variable is encapsulated in all classes of same package in java

# //when the variable is mareked as public is variable
# // isn't encapsulated its visible/accessible to all

# // we define boundaries using access modifiers
# // and that boundary is called as encapsulation

# Abstraction
# related to industry topic called Authorization
# ex: College hierarchy
# Owner -> Dean -> HoD -> Student
# this explain that each and every one above have
# different permissions
    
# presenting the relevant rights(data)
# hiding the irrelevant rights(data)
# this is called as abstraction
    
# refer to file Program3.java

# view is an example of abstraction in dbms



# Polymorphism
# Polymorphism can be defined as a capability of an object 
# to exist in Multiple Forms.

# Types of Polymorphism:
#   - Static Polymorphism: when a function call is determined at Compile Time.
#       eg. function overloading
#   - Dynamic or Runtime Polymorphism : when a function  call is determined at Runtime.
#       eg. of dynamic polymorphism : function overriding.
    
# refer to Program4.java

# // 3 rules:
# // 1. count of parameters must be different
# // 2. type of parameters must be different
# // 3. sequence of parameters must be different


# to avoid the remembering of different name function overloading is used.
    
# Rule:
# An Object of Base Class can be initialized with
# constructor of any Derived class
#   eg. Doctor doc = new Surgeon();
    







