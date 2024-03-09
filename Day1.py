print("use me to display Messages")
print("press shiftenter as shortkey to run")
print('it is ok to use single quotes')
print("It is also ok to use double quotes")
print("""Triple quotes
allows us to write
multiline
messages""")
# this is comment
# taking care of quotations with quotation using backslash
print('bro did u try CCD\'s Coffee its pathetic')
print("yes bro, try starbuck\'s coffee it is \"super\" amazing")

# Data Types in Python
# String

# String represents text data, it can be a combination of characters, numbers and symbols
# eg.
# "python@123"
# note: any thing in quotation is string.

#Int
# Integer represents whole numbers,
# eg.
# 10, 2, 44

#Float
# Float represents Decimal Values.
# eg.
# 2.2, 0.0001

#Bool
# Bool represents Logical Values i.e True and False (observe Capital T and F)

name='andika'
age=29
height=5.11
isIndian=False
print(name,age,height,isIndian)
print('how are you ', name)

#type()
#using type function to determine the variable's datatype

type(name)
type(age)
type(height)
type(isIndian)

#String Formatting
name='andika'
age=29
#Poor Method of preparing / formatting Strings
print('how are you ', name , ' you are ', age , ' years old')

# Method 1. using format() function
print("how are you {} you are {} years old ".format(name,age))
# this is . function every curly bracket replaces with respective variable in format

# positions can be changed
print("how are you {0} you are {1} years old ".format(name,age))
print("how are you {1} you are {0} years old ".format(name,age))



name='andika'
age=29

#Method 2 : % Expression
print("how are you %s you are %s years old " % (name,age))


#Method 3 : using F string
# Rule1 : Sentence must be prefixed with letter 'f'
# Rule2 : variables must be enclosed in {} brackets

print(f'how are you {name} you are {age} years old') # recommended method

#Activity

item='clock'
day='yesterday'
impact='time consuming'

print("I Ate a {} {} it was very {}".format(item,day,impact))
print("I Ate a %s %s it was very %s"%(item,day,impact))
print(f"I Ate a {item} {day} it was very {impact}")

# input / Output in Python

name = input('what is ur name ')
print(f'how are you {name}')

# practice exercise: slam Book

name = input('enter your name ')
city = input('enter your city ')
wish = input('enter your wish ')

summary=f'''
hello {name} ,
you are from {city} ,
and your wish is {wish}
'''
print (summary)

age = int(input('enter your age '))
print('your age is ', age, ' type is ', type(age))

# typecasting functions
# bool()
# int()
# float()
# str()



# Activity
# practice exercise (Pound to Kg Conversion)
lbs = int(input('enter weight in Pounds '))
kg = lbs * 0.45

print(f'{lbs} Pounds is {kg} kilograms')

# Accept BasePay from user
# check if basePay >= 5000
# then
# HRA is 12% of basePay
# DA is 14% of basePay
# if basePay < 5000
# then
# HRA is 16% of basePay
# DA is 18% of basePay

# find Gross Pay (sum of basePay + HRA + DA)

# solution

basePay = int(input('enter your base pay '))
if basePay > 5000 :
    HRA = .12 * basePay
    DA = .14 * basePay
else:
    HRA = .16 * basePay
    DA = .18 * basePay
grossPay = HRA + DA + basePay
salarySlip = f'''
Salary Slip
---------------------
BasicPay {basePay}
HRA {HRA}
DA {DA}
---------------------
Gross Pay : {grossPay}
'''
print(salarySlip)

# Handling Multiple Conditions using Elif

SP = int(input('enter selling price '))
CP = int(input('enter Cost Price '))

if SP == CP:
    print('breakeven')
elif SP > CP:
    print('Profit')
else:
    print('Loss')

# while loop demo
meter=1
while meter <= 10 :
    print(f' Counting from 1 to 10, Now at {meter}')
    meter+=1

# Range (LIMIT)
# this function is used to generate numbers,
# this function generates numbers from 0 to LImit -1
# eg.
# range(5) generates 0,1,2,3,4
    
for x in range(5):
    print(x)

for x in range(2,6):
    print(x)

for x in range(2, 9, 2):
    print(x)

# Activity

# step1: generate a random number between 1 and 20 sttore in a variable say computerChoicee
# step2: ask the user to enter a number between 1 and 20, store in a variable say userChoice
# step3: do the comparision
#     if userChoice > computerChoice print "your guess is too low"
#     if userChoice < computerChoice print "your guess is too hight "
#     if userChoice matches with computerChoice print "gotcha! u guessed it right"
# note: a user shall be provided with total 6 attempts to guess the random number (same rand. no. everytime)
# after 6 failed attempts the program prints "All attempts Exhausted Try later"

#solution
import random

attempts = 6
computerChoice = random.randint(1, 20)
    
while attempts > 0:
    userChoice = int(input("Enter a number between 1 and 20: "))
        
    if userChoice > computerChoice:
        print("Your guess is too high.")
    elif userChoice < computerChoice:
        print("Your guess is too low.")
    else:
        print("Gotcha! You guessed it right.")
        break
        attempts -= 1
    if attempts > 0:
        print(f"Attempts left: {attempts}")
    else:
        print("All attempts exhausted. Try later.")

#Activity
# How Long is your burp?
# Ask the user to enter burp length and produce 'burp'
# for eg.
# input: 5 output:'Burrrrrp'
# input: 25 output: 'Burrrrrrrrrrrrrrrrrrrrrrrrrp'
# note : any lenght can be entered by user.

# 'r'*5 don't use this method

#mySolution

burpLength = int(input("Enter the length of the burp: "))
print('Bu',end="")
for i in range(burpLength):
    print('r' ,end="")
print('p')

# ask the user to enter a number a find sum of all digits in a given number
# eg.
# 257 gives : 13 answer

num = int(input("Enter the number"))
total = 0
while num:
    last = num%10
    total += last
    num = num//10
print(total)

# take a number (says 'n') as an input.
# print the value of 'n'.
# while n!=1
# a) print the value of 'n'.
# b) if 'n' is odd, calculate the next number as n*3+1.
# c) if 'n' is even, calculate the next number as n/2.

# example:
# input: 10
# output (Hailstone Sequence): 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# input: 17
# output (Hailstone Sequence): 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1