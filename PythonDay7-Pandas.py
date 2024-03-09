# Creating DataFrame -> pd.read_csv('nba.csv')
# nba.columns.tolist()
# .describe() : returns statistical facts about all numerical columns.
# nba.isna().sum() -> we can use this expression to exactly find the count of missing values
# .head()       -> returns first 5 rows of the data
# .tail()       -> returns last 5 rows of the data
# nba['Name'].head(3) -> Accessing a single column
# bond.iloc[2:10:2] -> iloc is used for searching with default indexes
# bond.loc['GoldFinger'] -> loc is used for searching with labeled indexes
# .nunique(): returns count of unique values --> this doesn't include NaN when counting
# .unique(): returns unique values
# *** Important ***
# Broadcasting
#   -Broadcasting in Pandas is a capability that allows arithmetic 
#    operations to be performed between DataFrames and Series objects with different shapes, 
#    aligning their indices and dimensions automatically.
# Vectorization in numpy is called broadcasting in pandas



# What is Pandas?
# Pandas is a powerful and easy to use library primarily used for Data Analysis.
# Using Pandas You can do 
#   - Data Pre-Processing or Data Cleaning
#   - Data Manipulation
#   - Data Analysis (Primary)

# Pandas Provides its own Data Structures for storing and processing Data.
#   1. Series
#   2. DataFrame

# When to Use which one?

# Series
# Series is used to store and process 1D or Linear Data. eg like a list in Python.

# DataFrame
# DataFrame is used to store and process 2D or Tabular Data . eg like excel sheet

# Step 1 : import pandas
import pandas as pd

# sample data
prices = [10, 20, 30, 40, 50]

mySeries = pd.series(prices)

# what is mySeries?
type(mySeries)

# what does it contains?
print(mySeries)

# Quick Fact : Pandas Data Structures i.e Series/DataFrame uses ND Array
# Internally for Sorting and Processing Data.

# Confirmation
print(mySeries.values)

type(mySeries.values)

# pandas has access to nd array but not to numpy
# pandas internally uses nd array because it helps work fastly

# nd array provides only basic maths and array manipulations for pandas
# if we want complete mathematics we need to import numpy

print(mySeries.max())
print(mySeries.min())

# Creating DataFrame
nba = pd.read_csv('nba.csv')

# what is nba?
print(type(nba))

#what does it contains?
print(nba)

# nan represents missing values
# nan doesn't mean empty/blank

# Data Inspection

print(nba.shape)

# .column
print(nba.columns.tolist())

# .dataTypes
print(nba.dtypes)

# ** Note: Object Type Represents String Data in pandas **

# .describe() : returns statistical facts about all numerical columns.
print(nba.describe())

# .info()
print(nba.info())

# we can use this expression to exactly find the count of missing values
print(nba.isna().sum())

# .head()       -- returns first 5 rows of the data
print(nba.head())

# .tail()       -- returns last 5 rows of the data
print(nba.tail())

# to get the specified no.of rows
print(nba.head(3))

# Accessing a Single Column
# we can use two syntaxes
print(nba.Name.head(3))
print(nba['Name'].head(3))

# difference between above two is
# you cannot access columns having spaces in their title using (dot) expression.

# lets test it
# adding a new column
nba['my sport'] = 'basketball'

print(nba.head(3))

# deleting column
del nba['my sport']
print(nba.head(3))

# Accessing Multiple Columns
print(nba.head(3))

mycols = ['Name','College','Salary']
print(nba[mycols].head(3))

# Direct
print(nba[['Name','College','Salary']].head(3))

# Objective : You are asked to find players from a college named 'Texas'

# method 1
c1 = nba.College == 'Texas'
nba[c1]

# Direct Expression
nba[nba.College == 'Texas']

# Quick Activity:
# How many players are under the age of 25

under25 = nba[nba.Age < 25]
len(under25)

# Handling Multiple Conditions
# Objective: you are asked to find players from 'Texas' college palying for position 'PG'

c1 = nba.college == 'Texas'
c2 = nba.Position == 'PG'
nba[c1 & c2]    # here & is logical AND Operator

# Direct Expression
nba [ (nba.College == 'Texas') & (nba.Position == 'PG')]

# using OR
print(nba[(nba.Position == 'PF') | (nba.Position == 'C')])

# Finding all Players whose Salary is unavailable i.e NaN
print(nba[nba.Salary.isnull()])

# How would you find Players whose Salary is Available?
# opertors are applicable on values ex: !
# negation (~) is to apply on functions in place of not (!)
print(nba[~ nba.Salary.isnull()])

# Finding Players whose age is between 22 and 25
# Extracting Data in Range

print(nba[nba.Age.between(22,25)])

# Finding players whose age is not between 22 and 25
print(nba[~ nba.Age.between(22,25)])


# Sorting
# Descending
print(nba.sort_values(by = 'Age', ascending=False))

# Ascending
print(nba.sort_values(by = 'Age', ascending=True))

# You are asked to find the highest Paid Player playing from 'PG' Position and from TEam 'Memphis Grizzlies'
print(nba[(nba['Position'] == 'PG') & (nba['Team'] == 'Memphis Grizzlies')].sort_values(by='Salary', ascending=False).head(1))

# or
print(nba[(nba.Team == 'Memphis Grizzilies') & (nba.Position=='PG')].sort_values('Salary',ascending=False).head(1))

# SQL query for the same question
# select *
# from nba
# where team = 'Memphis Grizzlies' and position = 'PG'
# order by salary desc
# limit 1;

# Type Casting in Pandas
df = pd.read_csv('employees.csv')
print(df.head(3))

print(df[['Start Data','Last Login Time']].head())
print(df[['Start Date','Last Login Time']].dtypes)

# we can see dtypes as objects which means strings but data inside these
# columns are values of given columns

# so to type cast the values of the respective columns i.e, from object to date and time

df['Start Date'] = pd.to_datetime(df['Start Date'])
print(df[['Start Date','Last Login Time']].dtypes)
# we can see the type of data for above one for start date will be datetime64[ns]

print(df['Senior Manager'].dtype)
# this coloumn datatypes shows as object which is not correct
# this column actually stored boolean

# now typecast object to boolean
df['Senior Management'] = df['Senior Management'].astype('bool')
print(df['Senior Management'].dtype)

# .astype() : int/float/bool/object

df.head()

# Major Analytical Functions
# .nunique(): returns count of unique values --> this doesn't include NaN when counting
print(df.Gender.nunique())

# Find the count of Team in Data?


# .unique(): returns unique values
print(df.Gender.unique())

# Find the Name of Teams


# value_counts(): this function returns the frequency or occurence count of each unique value
print(df.Gender.value_counts())

# Find the count of Employees in Each Team?
team_employee_count = df.groupby('Team').size()
print("Count of Employees in Each Team:")
print(team_employee_count)

# Data Imbalance Check
# Normalize=True: converts the numbers into %age Distribution
print(df.Gender.value_counts(normalize=True)*100)

# How is the Employee Distribution(%) in terms of Senior vs Junior Employees?
print(df['Senior Management'].value_counts(normalize=True) *100)

# Working with Indexes
bond = pd.read_csv('jamesbond.csv')
print(bond.head())

# Accessing Rows using RowIndex
print(bond.iloc[2])

# Slicing Expression Show Off
print(bond.iloc[:4])
print(bond.iloc[2:6])
print(bond.iloc[[2,6,8]])
print(bond.iloc[22:])
print(bond.iloc[2:10:2])

# Replacing Default Row Index with a Column
# Setting 'Film' Column as Index

print(bond.head())
bond.set_index('Film',inplace=True)
print(bond.head())
print(bond.loc['GoldFinger'])

# loc is used for searching with labeled indexes
# iloc is used for searching with default indexes

# Reset Index
bond.reset_index(inplace=True)
print(bond.head())

# Set year column index column, find the movies produced in the year 1983
df.set_index('Year', inplace=True)
print(df.loc[1983])

# *** Important ***
# Broadcasting
# Vectorization in numpy is called broadcasting in pandas

print(nba.head(3))
print(nba.Salary / 1000000)

def convertToMillion(sal):
    return f'{round(sal/1000000,2)} Mil.'

print(nba.Salary.apply(convertToMillion))

print(nba.head())

print(nba.Weight.describe())

# You are asked to Categorize players based on their weight and Find the count of Each Weight Category
#   1. Weight > 240                 'overweight'
#   2. weight between 220 and 240   'normalweight'
#   3. weight < 220                 'underweight'

# solution
def getCategory( wgt ):
    if wgt > 240:
        return 'overweight'
    elif wgt >= 220 and wgt <=240:
        return 'normalweight'
    elif wgt<220:
        return 'underweight'
    
nba['category'] = nba.Weight.apply(getCategory)
print(nba.head())
print(nba.category.value_counts())


























