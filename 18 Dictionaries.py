# Python Dictionary
# Key:value pairs are contained in the dictionary as an ordered collection enclosed in curly brackets ‘{ }’ and separated by commas ‘ , ‘. 
# When the key is known, dictionaries are designed to retrieve values quickly.

# Dictionaries are versatile and widely used in Python for tasks that involve mapping keys to values, such as storing configuration settings, caching data, and more.

# Creating a Dictionary
# A dictionary can be made by enclosing a list of key-value pairs in curly braces ‘{ }’ and separating them with commas. 
# A colon ‘ : ‘ is used to separate each key-value pair.

# Creating a Dictionary
dict = {
    "name": "PrepInsta",
    "city": "Noida"
}
print(dict)

# Accessing the Values
# You can access the values in a dictionary by using the keys as the index.

#Accessing Value
dict = {
    "name": "PrepInsta",
    "city": "Noida"
}
print(dict['name'])

# Modifying Values
# You can change the value associated with a key in a dictionary by simply assigning a new value to that key.

#Modifying Values
dict = {
    "name": "PrepInsta",
    "city": "Noida"
}
dict["city"] = "New York"
print(dict)

# Adding New Key – Value Pair

#Adding new key value pair
dict = {
    "name": "PrepInsta",
    "city": "Noida"
}
dict["category"] = "edtech"
print(dict)

# Removing Key – Value Pair
# By following the key you want to delete with the del keyword, you can delete key-value pairs from a dictionary.

#Removing key value pair
dict = {
    "name": "PrepInsta",
    "city": "Noida"
}
del dict["city"] 
print(dict)

# Checking if a Key Exists
# You can check if a key exists in a dictionary using the in keyword.

#Checking if a key exists
dict = {
    "name": "PrepInsta",
    "city": "Noida"
}
if "name" in dict:
    print("Yes, This is in your dictionary")

# =========================================================================================

# count of distinct elements
arr = [1,2,3,3,2,4,5,1,2]
s = set()
for i in arr:
    s.add(i)
print(len(s))

# ==============================================================================================

# SORTING BY KEYS:

my_dict = {'b': 3, 'a': 1, 'c': 2}

# Sort the dictionary by keys
sorted_dict = dict(sorted(my_dict.items()))

print(sorted_dict)  # Output: {'a': 1, 'b': 3, 'c': 2}

# ================================================================================================

# SORTING BY VALUES:

my_dict = {'b': 3, 'a': 1, 'c': 2}

# Sort the dictionary by values
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# lambda item: item[1]: This is a lambda function, which is a small anonymous function. 
#                         In this case, it takes one argument item and returns item[1], 
#                         which means it extracts the second element (index 1) from each tuple item. 
#                         Remember that my_dict.items() returns a sequence of tuples where each 
#                         tuple contains a key-value pair from the dictionary.

# For example, if my_dict.items() yields ('a', 1), ('b', 2), ('c', 3), the lambda 
# function will return 1, 2, 3, respectively. This value will be used for 
# comparison during the sorting process.

# key=lambda item: item[1] is telling the sorted() function to sort the items based 
#                          on the values (the second element of each tuple) rather than the keys.

print(sorted_dict)  # Output: {'a': 1, 'c': 2, 'b': 3}

# In both cases, the sorted() function is used to sort the dictionary. 
# When sorting by keys, sorted() sorts the dictionary's items based on their keys by default. 
# When sorting by values, the key parameter is used to specify a function that extracts a 
# comparison key from each dictionary item, and the items are sorted based on those keys.

# Remember that dictionaries in Python 3.7 and later maintain insertion order, 
# so if you just need the dictionary in insertion order, you can simply use it as is 
# without sorting. If you need the dictionary sorted, you can use the above methods.

# ===================================================================================================

# Python program for Sorting elements of an array by frequency

arr = [30, 20, 30, 10, 20, 20]
dicts = {}
for i in arr:
    if i in dicts:
        dicts[i] = dicts.get(i) + 1
    else:
        dicts[i] = 1

print(dicts)

sorted_dict = dict(sorted(dicts.items(), key=lambda item: item[1],reverse=True))
print(sorted_dict)
result = []
for key in sorted_dict:
    for j in range(1,sorted_dict[key]+1):
        result.append(key)

print(result)

# ====================================================================================================

# count of distinct elements
s = set()
for i in arr:
    s.add(i)
print(len(s))

# ==================================================================================================

# Finding the frequency of element Frequency of elements in an array using Python
# dict.get(key): Accesses the value associated with the specified key, returns None if the key is not found
# dict[key] = value: Adds or updates the value associated with the specified key.
arr = [10, 30, 10, 20, 10, 20, 30, 10]
dict = {}
for i in arr:
    if i in dict:
        dict[i] = dict.get(i)+1
    else:
        dict[i] = 1

print(dict)




























