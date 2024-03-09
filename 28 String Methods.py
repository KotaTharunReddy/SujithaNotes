# Method	            Description	        Example

# capitalize()	returns a string copy with the first letter in uppercase	
text="hello"
text.capitalize()
# 'Hello'

# ========================================================

# casefold()	returns a string copy with the all letter in lowercase	
text="HELLO"
text.casefold()
# 'hello'

# ========================================================

# center()	returns a centered string copy	
text="HELLO"
text.center(10)
# ' HELLO '

# ============================================================

# count()	returns number of occurences of a specific value in the given string	
text="HELLO"
text.count('L')
# 2

# =============================================================

# encode()	returns encoded version of the string	
text="HELLO"
text.encode()
# b'HELLO'

# ============================================================

# endswith()	returns True if the given string ends with given value else returns False	
text="HELLO"
text.endswith('O')
# True

# ============================================================

# find()	returns 0 if the given sub-string is present else returns -1	
text="HELLO"
text.find('E')
# 0

# ===========================================================

# index()	returns the index of the element in the string, this method throws exception if the element is not present in the string.	
text="HELLO"
text.index('E')
# 1

# ===========================================================

# isalnum()	returns True if the given string contains only alpha-numeric values	
text="HELLO"
text.isalnum()
# True

# ===========================================================

# isalpha()	returns True if string contains only alphabets	
text="HELLO"
text.isalpha()
# True

# ===========================================================

# isdigit()	returns True if the string contains only digits else returns False	
text="HELLO"
text.isdigit()
# False

# ===========================================================

# isidentifier()	returns True if the string only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.	
text="HELLO"
text.isidentifier()
# True

# # ===========================================================

# islower()	returns True if the string contains all the characters are in lowercase	
text="hello1"
text.islower()
# True

# # ===========================================================

# isnumeric()	returns True if all the characters in the string are numrical else returns False	
text="HELLO"
text.isnumeric()
# False

# ===========================================================

# isspace()	returns True if the string contains whitespaces only	
text="hello1"
text.isspace()
# False

# ===========================================================

# isupper()	returns True if the string contains all the characters are in uppercase	
text="HELLO1"
text.isupper()
# True

# ===========================================================

# lower()	returns a copy of string with all characters in lowercase	
text="HELLO"
text.lower()
# 'hello'

# ===========================================================

# partition()	returns a tuple with 3 strings partitioned by the argument	
text="HELLO"
text.partition('L')
# ('HE','L','LO')

# ===========================================================

# replace()	returns a copy of string with a specific value replaced by another given value	
text="HELLO"
text.replace("L","l")
# 'HEllO'

# ===========================================================

# split()	returns a list of strings splited by whitespaces by default if no character is passed as arguments	
text="Hello Prepsters! Welcome to Python Tutorials "
text.split()
# ['Hello','Prepsters!','Welcome,'to','the','Python','Tutorials']
 
# # ===========================================================

# upper()	returns a copy of string with all characters in uppercase	
text="hello"
text.upper()
# 'HELLO'