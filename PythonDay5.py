# Contents
# File Handling
# myfile = open('d:\\test.txt', 'w') # open(filePath), 'w' write mode
# myfile.write('i am the earth \n') # write for writing data in file
# myfile.flush() # for forcing write
# myfile.close()
# myfile = open('d:\\test.txt', 'a') -> to prevent file overriding use append mode
# myfile = open('d:\\test.txt','r') # read mode (default)
# data = myfile.read() # fetches all content of file as string
# data = myfile.readlines() # returns list where each line is a list element

#Exercise

partyVotes= "A,A,B,A,B,C,C,C,C,C,C,A,C,B,A,A,C,C,C,A,A,A,B,B,C,C,C,B,B,B"

# 1. Find unique parties
# 2. vote count for each party 

uniqParties = set(partyVotes.split(','))
print(uniqParties)

votes = partyVotes.split(',')
for party in uniqParties:
    print(party, votes.count(party))

email="ivor.horton@oracle.com" 
# extract onlyusername without .split() in python

email = "tharunreddykota2001@gmail.com"
index = email.index('@')

username = email[:index]

print(username)

# Recently it was Aniket Birthday

# below is the height of candles used in his birthday
candles = [6,4,4,2,6,3,6,6,2]

# you are asked to find the count of tallest candle. answer: 4
# note: you cannot use max() function here

candles = [6, 4, 4, 2, 6, 3, 6, 6, 2]
tallest_height = 0
count_tallest = 0
for height in candles:
    if height > tallest_height:
        tallest_height = height
        count_tallest = 1
    elif height == tallest_height:
        count_tallest += 1

print(count_tallest)

# Cup Swapping 

def cup_swapping(operations):
    current_position = "B"

    for move in operations:
        if current_position in move:
            if current_position == move[0]:
                current_position = move[1]
            else:
                current_position = move[0]
    return current_position

operations = ['AB', 'CA', 'AB'] 
print(cup_swapping(operations))

# Rajan's encryption Algorithm

# Write code that encryptes a given input with these steps

# Input: 'apple'

# Step1: Reverse the input : 'elppa'

# Step2: Replace all vowels using the following chart:

# a=>0

# e=>1

# i=>2

# 0=>3

# u=>4

# '11ppe'

# Step3: Add "aca" to the end of the word: '11pp@aca'

# end of exercise

# sample test cases

# input: banana -> 'Ononobaca'

# input: 'karaca' -> 'ecorokaca'

def encrypt(input_str):
    reversed_str = input_str[::-1]

    vowel_dict = {'a': '0', 'e': '1', 'i': '2', 'o': '3', 'u': '4'}
    replaced_str = ''.join(vowel_dict[char] if char in vowel_dict else char for char in reversed_str)
    
    encrypted_str = replaced_str + 'aca'
    
    return encrypted_str


test_cases = ['apple']
for input_str in test_cases:
    encrypted_str = encrypt(input_str)
    print(f"Input: {input_str} -> {encrypted_str}")

# sir solution
    
def encrypt(wd):
    rvrsd_wd = wd[::-1]

    vwls_to_num = {'a': '0', 'e': '1', 'i': '2', 'o': '3', 'u': '4'}
    
    for k in vwls_to_num:
        rvrsd_wd=rvrsd_wd.replace(k, vwls_to_num[k])

    encrypted_wd = rvrsd_wd + 'aca'

    return encrypted_wd
encrypt('apple')

# File Handling

# writing data in file
# if the file is already present it will be overwritten 

myfile = open('d:\\test.txt', 'w') # open(filePath), 'w' write mode

myfile.write('i am the earth \n') # write for writing data in file
myfile.write('i am forest green \n')
myfile.write('i am the earth \n')

myfile.flush() # for forcing write
myfile.close()
print('success')

# to prevent file overriding use append mode

myfile = open('d:\\test.txt', 'a') # open(filePath), 'w' write mode

myfile.write('i am forest green \n') # write for writing data in file
myfile.write('i am four winds blowing \n')
myfile.write('i am the earth \n')

myfile.flush() # for forcing write
myfile.close()
print('success')

# Reading File
myfile = open('d:\\test.txt','r') # read mode (default)
data = myfile.read() # fetches all content of file as string
print(data)
myfile.close()

myfile=open('d:\\test.txt','r') # read mode (default)
data = myfile.readlines() # returns list where each line is a list element
print(data)
myfile.close()

# Google Stocks Case Study\
# note : you cannot use min/max/sum function.
# Dataset Link:
# https://drive.google.com/file/d/1D3UKCfDheTjFcPiY91MPmSnkGu7q3KND/view?usp=drive_link
# google_stock_price file in wileyedge folder
# Objectives:
# find the largest Stock value
# find the smallest Stock value
# find the sum of all stocks
# find the mean stock value
# find the median stock value

myfile=open('c:\\downloads\\google_stock_price','r') # read mode (default)
data = myfile.readlines() # returns list where each line is a list element
print(data)
myfile.close()





