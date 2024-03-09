# Contents

# LISTS
#   => len()     to find length of the list
#   -> .append() Adding
#   -> .insert() Adding using index
#   -> .extend() Adding multiple
#   -> .remove() Using name
#   -> .del()    Using index (can delete multiple - using slicing)
#   -> .pop()    Deletes last (deletes using index also - one element at a time- returns deleted value)
#   -> .sort()   sorts in place returns void | works only with list
#   -> .sorted() sorts and return new list works for all sequences

# TUPLES
#   -> only can be created no modifications allowed
#   -> list element inside tuple can be modified but can't entirely be deleted.

# Data Structures
# Data Structures enables us to store, organize, access and manipulate Data Efficiently.
# Types of Data Structures
# 1. Primitive Types
#       1.1 Int
#       1.2 Str
#       1.3 Float
#       1.4 Bool
# 2. Non-Primitive Types
#       2.1 List
#       2.2 Tuple
#       2.3 Set
#       2.4 Dictionary

# list data structure
grocery = ['milk','bread',100,100,100,True,False,10.4,[1,2,3]]

# Characteristics of List
#  A list is represented using [].
#  A list can contain duplicates.
#  A list can contain values of Mixed Data Types, it is called Compound Nature.
#  A list is a mutable Data structure, it means we can make modifications in list element.
#   eg. Add element
#       Update element
#       Delete Element
#       Sort Elements
#  A list is an Ordered Collection, it means the sequence in which we add elements we get the same sequence when fetching elements.

# Simulating Shopping_Cart As List
# This Demo Explains Various List Operations.

# creating empty List
shopping_cart = []
print(f'Total Items in CART {len(shopping_cart)}')

# Adding Element in a List using .append()
# syntax: listname.append(valueHere)

shopping_cart.append('iPhone')
shopping_cart
shopping_cart.append('airPods')
shopping_cart.append('iPad')
shopping_cart.append('harman-kardon')
shopping_cart.append('macbook')
print(shopping_cart)
print(f'Total Products in CART {len(shopping_cart)}')


# Accessing Element using Index

shopping_cart
shopping_cart[0]
shopping_cart[-1]

# when is negative indexing is useful?
# when a form being filled by users might be any form
# and last detail is salary
# when someone properly fills the form the data is like:
# X,X,X,X,X
# or left something by user it looks like:
# X,,,X,X
# we can see no.of coloumns in each form is different.
# in this case -1 is helpful access the last element no matter
# the no.of columns present.

# Adding Element at a Desired Position using .insert()
print(shopping_cart)
shopping_cart.insert(2,'bose')
print(shopping_cart)

# Adding Multiple Elements in a list using Extend()

print(shopping_cart)
#new list
combo_offer = ['bagpack','charger','dumbell']
shopping_cart.extend(combo_offer)
print(shopping_cart)

# Let us learn the difference between append() vs extend()

l = [1,2,3,4]
print(l)            # -> 1
l.extend([5,6,7])   
print(l)            # -> 2
a = [8,9,10]
l.append(a)         
print(l)            # -> 3
e = [11,12,13]
l.extend(e)         
print(l)            # -> 4

# output
# [1, 2, 3, 4]                                      # -> 1
# [1, 2, 3, 4, 5, 6, 7]                             # -> 2
# [1, 2, 3, 4, 5, 6, 7, [8, 9, 10]]                 # -> 3
# [1, 2, 3, 4, 5, 6, 7, [8, 9, 10], 11, 12, 13]     # -> 4


# Removing Element from a List
# method 1 : using .remove()
print(shopping_cart)
shopping_cart.remove('harman-kardon')
print(shopping_cart)

# method 2 : using del keyword
# del requires index to delete

print(shopping_cart)
del shopping_cart[2]
print(shopping_cart)

# Summary:
#   .remove() requires value to delete an element
#   we cannot remove multiple elements using .remove() method.
#   del requries index to delete the element.
#   we can delete multiple elements using del, this requires slicing to be used.

# method 3 : using .pop()
print(shopping_cart)
cancelled_product = shopping_cart.pop()
print('you cancelled ', cancelled_product)

# 1. Pop() method deletes the Last Element.
# 2. Pop() works with Index also.
# 3. You cannot Delete Multiple Elements using .Pop()
# 4. (primary) Pop method returns the Deleted Element.

print(shopping_cart) # dumbell is deleted

returnedProduct = shopping_cart.pop(2)
print(returnedProduct) # prints iPad
print(shopping_cart)

# point 1 above means it returns only one element at a time.

# Sorting

print(shopping_cart)
sortedCart = sorted(shopping_cart)
print(sortedCart)
print(shopping_cart)
# sorted function doesn't sorts the original List, it returns a new Sorted List.

shopping_cart.sort() # this function sorts original list and returns void
print(shopping_cart) # observe the source list is sorted

# Traversing through each element of list using for loop
for product in shopping_cart:
    print(product)

# Tuple
# Tuple is known for its READ ONLY nature, it means once a tuple is created
# its elements cannot be modified or manipulated

# Tuple is represented using ()
# Tuple can contain Duplicates & Mixed DataType Elements too.
    
panCards = ('AONJK444K', 'IBQK222521', 'MCQJ22921')
type(panCards)

# Tuple can contain duplicates and mixed type of elements

# here is a confimation that tuple is READONLY
del panCards[0]           # TypeError: 'tuple' object doesn't support item deletion
panCards[0] = 'SIHF737EJ' # TypeError: 'tuple' object does not support item assignment
# above line outputs error when you run it.

# tuple is faster than list when accessing the elements
# internally tuple elements stored at same place
# where as list elements are stored internally in jumbled and random way

# Unpacking
# easiest way to extract elements from tuple

card1, card2, card3 = panCards
print(card1)
print(card2)
print(card3)

car = (10)
print(type(car)) # produces type as 'int'
cars = (10,) # produces type as 'tuple'

garbage= (10,20,['delhi','madras','meerut'],30,40)
# can we change the list elements inside a Tuple ! Test

garbage[2][1]='Chennai' # changes madras to chennai
# hence we can change list elements inside a tuple.
# we cannot delete the entire list but can modify the 
# elements present in it.









