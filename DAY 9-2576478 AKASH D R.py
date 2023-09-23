#!/usr/bin/env python
# coding: utf-8

# # 1. Create a 3x3x3 array with random values

# In[2]:


import numpy as np

# Create a 3x3x3 array with random values
random_array = np.random.rand(3, 3, 3)

print(random_array)


#  # 2.Create a 5x5 matrix with values 1,2,3,4 just below the diagonal

# In[4]:


import numpy as np

# Create a 5x5 matrix filled with zeros
matrix = np.zeros((5, 5))

# Fill the values just below the diagonal
values = [1, 2, 3, 4]
for i in range(1, len(values) + 1):
    matrix[i, i - 1] = values[i - 1]

print(matrix)



# # 3.Create a 8x8 matrix and fill it with a checkerboard pattern

# In[5]:


import numpy as np

# Create an 8x8 matrix filled with zeros
checkerboard = np.zeros((8, 8))

# Fill the even rows and columns with 1
checkerboard[::2, ::2] = 1
checkerboard[1::2, 1::2] = 1

print(checkerboard)


# # 4. Normalize a 5x5 random matrix

# In[6]:


import numpy as np

# Create a 5x5 random matrix
random_matrix = np.random.rand(5, 5)

# Calculate the mean and standard deviation of the matrix
mean = np.mean(random_matrix)
std_dev = np.std(random_matrix)

# Normalize the matrix
normalized_matrix = (random_matrix - mean) / std_dev

print("Original Matrix:")
print(random_matrix)

print("\nNormalized Matrix:")
print(normalized_matrix)


# # 5. How to find common values between two arrays?

# In[7]:


import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([3, 4, 5, 6, 7])

common_values = np.intersect1d(array1, array2)
print(common_values)


# # 6. How to get the dates of yesterday, today and tomorrow?

# In[8]:


import numpy as np
from datetime import datetime, timedelta

# Get the current date (today)
today = datetime.now()

# Calculate the dates of yesterday and tomorrow using NumPy
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

# Convert the dates to NumPy datetime64 objects
today_np = np.datetime64(today)
yesterday_np = np.datetime64(yesterday)
tomorrow_np = np.datetime64(tomorrow)

print("Yesterday:", yesterday_np)
print("Today:", today_np)
print("Tomorrow:", tomorrow_np)


# # 7. Consider two random array A and B, check if they are equal

# In[9]:


import numpy as np

# Generate two random arrays A and B
A = np.random.rand(3, 3)
B = np.random.rand(3, 3)

# Check if the arrays are equal
are_equal = np.array_equal(A, B)

if are_equal:
    print("Arrays A and B are equal.")
else:
    print("Arrays A and B are not equal.")


# # 8.Create random vector of size 10 and replace the maximum value by 0

# In[10]:


import numpy as np

# Create a random vector of size 10
random_vector = np.random.rand(10)

# Find the index of the maximum value
max_index = np.argmax(random_vector)

# Replace the maximum value with 0
random_vector[max_index] = 0

print("Random Vector with Maximum Value Replaced:")
print(random_vector)


# # 9. How to print all the values of an array?

# In[11]:


import numpy as np

my_array = np.array([1, 2, 3, 4, 5])
print(np.array_str(my_array, max_line_width=np.inf))


# # 10.Subtract the mean of each row of a matrix

# In[12]:


import numpy as np

# Create a sample matrix (replace this with your own matrix)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Calculate the mean of each row
row_means = np.mean(matrix, axis=1)

# Subtract the row means from the matrix
normalized_matrix = matrix - row_means.reshape(-1, 1)

print("Original Matrix:")
print(matrix)

print("\nMatrix with Row Means Subtracted:")
print(normalized_matrix)


# # 11.Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)?

# In[13]:


import numpy as np

# Given vector
given_vector = np.array([1, 2, 3, 4, 5])

# Index vector (with repeated indices)
index_vector = np.array([0, 2, 2, 4])

# Create a mask to handle repeated indices
mask = np.zeros_like(given_vector, dtype=bool)
mask[index_vector] = True

# Add 1 to the elements at the specified indices
given_vector[mask] += 1

print("Given Vector with 1 Added to Elements at Specified Indices:")
print(given_vector)


# # 12.How to get the diagonal of a dot product?

# In[14]:


import numpy as np

# Create two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Calculate the dot product of A and B
dot_product = np.dot(A, B)

# Get the diagonal of the dot product
diagonal = np.diag(dot_product)

print("Dot Product:")
print(dot_product)

print("\nDiagonal of Dot Product:")
print(diagonal)


# # 13.How to find the most frequent value in an array?

# In[15]:


import numpy as np

# Create an array
x = np.array([7, 4, 5, 3, 3, 6, 5, 8, 1, 5, 1, 1, 8, 7, 4, 5, 8, 7, 3, 2, 3, 6, 1, 5, 3, 3, 7, 5, 0, 3, 8, 7, 1, 4, 1, 4, 1, 1, 1, 6, 6, 8, 6, 8, 3, 4, 4, 7, 8, 0])

# Find the most frequent value
most_frequent_value = np.bincount(x).argmax()

print("Array:")
print(x)

print("\nMost Frequent Value:", most_frequent_value)


# # 14. How to get the n largest values of an array

# In[16]:


import numpy as np

# Create an array
arr = np.array([23, 34, 121, 23, 22, 67, 686, 434, 123])

# Get the 3 largest values
n_largest_values = np.partition(arr, -3)[-3:]

print("Original Array:")
print(arr)

print("\n3 Largest Values:")
print(n_largest_values)


# # 15. How to create a record array from a regular array?

# In[17]:


import numpy as np

# Create a regular array
regular_array = np.array([(1, 'Alice', 25),
                          (2, 'Bob', 30),
                          (3, 'Charlie', 22)],
                         dtype=[('id', 'i4'), ('name', 'U10'), ('age', 'i4')])

print("Regular Array:")
print(regular_array)

# Accessing fields in the record array
print("\nFirst row:")
print(regular_array[0])

print("\nName column:")
print(regular_array['name'])


# # 16. How to swap two rows of an array

# In[18]:


import numpy as np

# Create a sample array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Swap rows 0 and 1
arr[0], arr[1] = arr[1], arr[0]

print("Array with Rows Swapped:")
print(arr)


# # 17.Reshape to the next dimension of a numpy array

# In[19]:


import numpy as np

# Create a 2D array
x = np.array([[23, 34, 121],
              [23, 22, 67],
              [686, 434, 123]])

# Reshape it to a 3D array
y = x.reshape(x.shape + (1,))

print("Original 2D Array:")
print(x)

print("\nReshaped 3D Array:")
print(y)

