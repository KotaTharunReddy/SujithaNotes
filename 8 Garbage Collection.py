# Python follows two approaches for memory management in the programming language:

# Reference Counting
# Garbage collection

# Now users don’t have to use pre-allocate or de-allocate memory like dynamic memory allocation in languages like C, or C++. 
# This feature was inherited by the ABC programing language which is considered as the successor of the Python programming language.

# Reference Counting

# In the python version, 2.x python uses Reference counting for memory management. 
# Reference counting is done by counting the number of objects is referred by another object. 
# As the reference of the object is removed the count of the object is de-allocated. 
# As the reference count is decreased to 0 the object will be de-allocated.

# The memory of the object or variable is freed only when the scope of the variable or object is over. 
# Until the variable or an object is inside the scope it will not be cleared.

# Garbage Collection

# Garbage collection in python programming as the automatic scheduled memory management tool. 
# Garbage collection in python is scheduled upon a threshold of object allocation and object de-allocation. 
# The garbage collection runs when the number of object allocation, the number of object de-allocation is greater than the threshold. 
# The threshold of the garbage collection in python can be checked by some python commands.

import gc
print('Threshold is:', gc.get_threshold())



















