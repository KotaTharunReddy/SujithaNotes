# SET
# Set is known for storing unique Elements only.
# Set Eliminates Duplicates Automatically.
# Set is Unordered Collection.
# Set do not support Indexing.
# Set is Mutable Data Structure.
# Set is represented using {}
# Methods:
# .add()
# .remove()
# .intersection()
# .difference()
# .union()
# .symmetric_difference()

# DICTIONARY
# Adding key/vlaue Pair : syntax: dict[keyhere] = valueHere
# del key[value]
# .get()
# .keys()  returns keys onlly
# .values() returns values only
# .items() returns key/value in a Tuple

# STRING
# .upper() -> converts all chars to Upper letters
# .lower() -> converts all chars to Lower letters
# .capitalize() -> makes only first character Capital
# .title() -> changes every word first character in the string to capital
# .index('r') -> gets index position of 'r'
# .startswith('c') -> return T or F whether string starts with 'c' or not
# .isdigit()
#   -this function tells if a variable contains Number and is Convertible to Integer
#   -it test for number character only but it tells if it is convertible. isdigit('123') returns T, isdigit('12 3') returns F.
# .split() -> to convert string to list
# .join() -> to convert list to string

fruits= {'apple', 'apple', 'orange','kiwi','kiwi','grapes'}
print(fruits)

# Adding & Removing Elements from Set

fruits.add('dragonfruit')
print(fruits)
fruits.remove('grapes')
print(fruits)

# it prints elements in sequence only if elements are of same type
checking = {1,2,3,4,5}
print(checking)

# it prints elements differently when elements are of different type
checking = {'one',1,2,3,'zero',4,5}
print(checking)

# Mathematical Implementation of SET

shinchenFans = {'rajat' , 'aniket' ,'priyal' ,'priyanshu','alekya'}
doremonFans = {'kartik','rajat','alekya','sejal','vidhi','aniket','nithigna'}
# Task 1 : You are asked to find people who like both shinchen and doremon
# Answer : Intersection : intersection help us find common Elements.

print(shinchenFans.intersection(doremonFans))
# alternatively
print(shinchenFans & doremonFans)

# Task 2 : You are asked to find commited shinchenFans only
# commited are those who only like shinchen

shinchenFans = {'rajat' , 'aniket' ,'priyal' ,'priyanshu','alekya'}
doremonFans = {'kartik','rajat','alekya','sejal','vidhi','aniket','nithigna'}

# answer : Difference : this extracts Elements of First Set only excluding Commons

print(shinchenFans.difference(doremonFans))

# Task 3 : You are asked to find Elements from Both sets

# answer : UNION : union merges 2 sets into 1 set

print(shinchenFans.union(doremonFans))
print(shinchenFans | doremonFans)

# Task 4 : You are asked to Find Commited Fans from both Sets
# answer : Symmetric_difference : Symmetric_difference find all elements from both sets EXCLUDING Commons.

print(shinchenFans)
print(doremonFans)
print(shinchenFans & doremonFans)
print(shinchenFans.symmetric_difference(doremonFans))
print(shinchenFans ^ doremonFans)

# intersection : finds only common elements from 2 sets
# union : fetches all elements from 2 sets including commons
# difference : fetches elements from first set only excluding commons.
# Symmetric_difference : fetches all elements from 2 sets excluding commons.

# Dictionary
# Dictionary is a special Data Structure where each element is a key/value pair

lang = {'en' : 'english', 'hi': 'hindi', 'fr':'french','es':'spanish'}
print(lang)

# Characteristics of Dictionary
#   - Keys cannot be repeated in a Dictionary.
#   - Only Immutable Types Can be used as Keys eg. int/float/str/bool/tuple
#   - Value can be of any dataType.
#   - Dictionary is Ordered Collection
#   - Dicitonary is Mutable Data Structure.

# Creating an empty dictionary
usa = {}

# Adding key/vlaue Pair : syntax: dict[keyhere] = valueHere

usa['Tx'] = 'Texas'
usa['Ca'] = 'California'
usa['Ar'] = 'Arkansas'
usa['Al'] = 'Alabama'
usa['Il'] = 'Illinois'

print(usa)
# Deleting key/value pair
del usa['Il']
print(usa)

# Getting a value using Key

print(usa)

# method 1:
usa['Tx']

# method 2:
usa.get('Tx')

# Differences: 
#   [] throws Error if a non existing key is provided
#   .get() method doesn't throws error when a non existing key is provided.
#   .get() method has a provision to produce a default value when a non existing key is found
#   syntax : .get('keyhere','default value here')

usa.get('Ca', 'Grrr... key Not Found')

usa.get('xoxo', 'Grrr... Key Not Found')

# Some useful methods of Dictionary

print(usa.keys()) # returns keys onlly
print(usa.values()) # returns values only
print(usa.items()) # returns key/value in a Tuple

# Looping Through Dictionary

# method 1 
for key in usa : #note : when a dict is used in loop it returns key by default
    print(key, usa[key], usa.get(key)) # develop flexibility here

# method 2 : using.items()
for key, value in usa.items(): # here each key/value is returned as Tuple and is unpacked
    print(key, value)

# Generating a Dictionary using a LOOP
# key : number
# value : square
    
mydict = {}
for x in range (2,11):
    mydict[x] = x* x #x is key, x* x is value
print(mydict)

# another example
# key : score
# value : 'pass' or 'fail', any score >45 is pass otherwise fail

marks = [29, 65, 54, 19, 28, 75]
reportCard = {}
for score in marks:
    if score > 45:
        reportCard [ score ] = 'Pass'
    else:
        reportCard [ score ] = 'Fail'
print(reportCard)

# String Operations

msg="crocODilE"
print(msg[0],msg[-1])

print(msg.upper(), msg.lower(), msg.capitalize(),msg.title(),msg.index('r'))

print(msg.startswith('c'), msg.startswith('t'))

test="this is so cool"
test.capitalize()
test.title()

# isdigit()
# this function tells if a variable contains Number and is Convertible to Integer
# it test for number character only but it tells if it is convertible.

lottery="283"
lottery.isdigit()

lottery="28 3"
lottery.isdigit()

# String Slicing
# Extracting a Portion of a Stirng i.e Substring

# enumerate returns a tuple where [0] is index [1] is element

# for c in enumerate('rajan'):

#   c (0,'r')
#   c (1,'a')
#   c (2,'j')
#   c (3,'a')
#   c (4,'n')

word = 'elizabeth'
for tup in enumerate(word):
    print(tup[1], end=' ')
    print(tup[0], end= ' ')
    print()

# var [ Start : End] # here End Index is excluded
print(word[1:5])

# var [ : End] # when start index is skipped default is 0
word[ : 4]

# var [ Start : ] # when end index is skipped default end index is length-1
word[5:]

# var [:] # it includes all indexes start to end
word[:]

# advance: var [start : end : step]
word[1:7:2]

word[0:8:3]

word[::-1] # use negative step for reversing string.

# Important:
# Converting String to List

wish = "One Day I'll Make Onion Cry"
print(wish.split())

# split converts string to list 
# by defaults it splits based on spaces

heroes = "hulk,ironman,spiderman,thor,thanos,superman"
avengers=heroes.split(',')

print(avengers)

spaceCount=0
for c in "One Day I'll Make Onion Cry":
    if c == ' ':
        spaceCount+=1
print(spaceCount+1)

spaceCount=0
for c in "One Day I'll Make Onion Cry":
    if ord(c) == 32: # ord() is used to find the ascii value of a character and checking it with ascii value of space i.e, 32
        spaceCount+=1
print(spaceCount+1)

# Converting List to String

' '.join(avengers)

scientists= "Georg Simon Ohm,Max Planck,Neils Bohr & Rutherford,Albert Einstein"

# Expected answer : 
#     Dear Mr. Ohm.G
#     Dear Mr. Planck.M
#     Dear Mr. Rutherford.N
#     Dear Mr. Einstien.A

for fullName in scientists.split(','):
    print(f'Dear Mr. {fullName.split()[-1]}.{fullName[0]}')










