#!/usr/bin/env python
# coding: utf-8

# 
# # 1 . Write a Python program to find a target values in a list using linear search with following steps:
# Initialize the list to store the input elements.
# b. Initialize found-False.
# c.
# Enter the item to be searched (match item).
# d. For each element in the list
# 1 if match item value
# a return match item's position.
# e. If the match item is not in the list, display an error message that the item is not found in
# the list

# In[4]:


def linear_search(arr, target):
    found = False  # Initialize found as False
    for index, element in enumerate(arr):
        if element == target:
            found = True  # Set found to True if the target is found
            return index  # Return the index of the target if found
    
    if not found:
        return -1  # Return -1 if the target is not found

# Initialize an empty list to store input elements
my_list = []

# Prompt the user to enter elements and add them to the list
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)

# Prompt the user to enter the target value
target_value = int(input("Enter the target value to search for: "))

# Perform the linear search
result = linear_search(my_list, target_value)

# Check the result and display the appropriate message
if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print(f"Target {target_value} not found in the list")


# # 2. Write a Python program to implement binary search to find the target values from the list
# a. Create a separate function to do binary search
# b
# Get the number of inputs from the user.
# c.
# Store the inputs individually in a list.
# d.
# In binary search function at first sort the list in order to start the search from middle of the
# e. Compare the middle element to right and left elements to search target element.
# f.
# If greater, move to right of list or else move to another side of the list.

# In[7]:


def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Define the search range
    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index
        mid_value = arr[mid]  # Get the middle element
        
        if mid_value == target:
            return mid  # Target found, return the index
        elif mid_value < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half
    
    return -1  # Target not found in the list

# Get the number of inputs from the user
n = int(input("Enter the number of elements: "))

# Store the inputs individually in a list
my_list = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    my_list.append(element)

# Sort the list to perform binary search (assuming the list is initially unsorted)
my_list.sort()

# Prompt the user to enter the target value
target_value = int(input("Enter the target value to search for: "))

# Perform binary search
result = binary_search(my_list, target_value)

# Check the result and display the appropriate message
if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print(f"Target {target_value} not found in the list")


# # 3. Write a Python program for sorting a list of elements using selection sort algorithm:
# a
# Assume two lists: Sorted list- Initially empty and Unsorted List-Given input list.
# h. In the first iteration, find the smallest element in the unsorted list and place it in the sorted
# e.
# list
# In the second iteration, find the senallest element in the unsoned list and place it in the correct position by comparing with the element in the sorted list.
# In the third iteration, again find the smallest element in the unsorted list and place it in the
# correct position by comparing with the elements in the sorted list.
# e.
# This process continues till the unsorted list becomes empty,
# Display the sorted list

# In[10]:


def selection_sort(arr):
    sorted_list = []  # Initialize an empty sorted list

    while arr:  # Continue until the unsorted list is empty
        smallest = min(arr)  # Find the smallest element in the unsorted list
        sorted_list.append(smallest)  # Append the smallest element to the sorted list
        arr.remove(smallest)  # Remove the smallest element from the unsorted list

    return sorted_list

# Get the number of inputs from the user
n = int(input("Enter the number of elements: "))

# Initialize an empty list to store input elements
unsorted_list = []

# Prompt the user to enter elements and add them to the unsorted list
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    unsorted_list.append(element)

# Perform selection sort
sorted_list = selection_sort(unsorted_list)

# Display the sorted list
print("Sorted list:", sorted_list)


# # 4. Write a Python program for sorting a list of elements using insertion sort algorithm:
# a. Assume two lists: Sorted list- Initially empty and Unsorted List-Given input list.
# h. In the first iteration, take the first element in the unsorted list and insert it in Sorted list
# c.
# In the second iteration, take the second element in the given list and compare with the element in the sorted sub list and place it in the correct position.
# d. In the third iteration, take the thind element in the given list and compare with the
# elements in the sorted sub list and place the elements in the correct position.
# e. This process continues until the last element is inserted in the soned sub list.
# f. Display the sorted elements.
# 

# In[11]:


def insertion_sort(arr):
    sorted_list = []  # Initialize an empty sorted list

    for element in arr:
        # Find the correct position to insert the current element in the sorted list
        i = 0
        while i < len(sorted_list) and element > sorted_list[i]:
            i += 1

        # Insert the current element at the correct position in the sorted list
        sorted_list.insert(i, element)

    return sorted_list

# Get the number of inputs from the user
n = int(input("Enter the number of elements: "))

# Initialize an empty list to store input elements
unsorted_list = []

# Prompt the user to enter elements and add them to the unsorted list
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    unsorted_list.append(element)

# Perform insertion sort
sorted_list = insertion_sort(unsorted_list)

# Display the sorted list
print("Sorted list:", sorted_list)


# # 5. Write a Python program that performs merge sort on a list of numbers:
# a. Divide: If the given array has zero or one element, return.
# 1. Otherwise
# Mphasis
# The Next Applied
# ii. Divide the input list in to two halves each containing half of the
# elements. i.e. left half and right half.
# b. Conquer: Recursively sort the two lists (left half and right half).
# a.
# Call the merge sort on left half.
# b.
# Call the merge sort on right half.
# c. Combine: Combine the elements back in the input list by merging the two sorted lists into a sorted sequence.

# In[12]:


def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # If the list has zero or one element, it's already sorted

    # Divide the input list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combine the sorted halves back into a sorted sequence
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from both left and right lists
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

# Get the number of inputs from the user
n = int(input("Enter the number of elements: "))

# Initialize an empty list to store input elements
input_list = []

# Prompt the user to enter elements and add them to the input list
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    input_list.append(element)

# Perform merge sort
sorted_list = merge_sort(input_list)

# Display the sorted list
print("Sorted list:", sorted_list)


# # 6. Write a Python script to perform the following operations on a singly linked list
# a.
# Create a list
# b. Find the smallest element from the list
# e.
# Insert an element if it is not a duplicate element
# d.
# Display the elements in reverse order

# In[13]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_smallest(self):
        if not self.head:
            return None

        smallest = self.head.data
        current = self.head.next

        while current:
            if current.data < smallest:
                smallest = current.data
            current = current.next

        return smallest

    def insert_unique(self, data):
        if not self.head:
            self.head = Node(data)
            return

        current = self.head

        # Check if the element already exists in the list
        while current:
            if current.data == data:
                return  # Element already exists, do not insert
            if not current.next:
                break
            current = current.next

        new_node = Node(data)
        current.next = new_node

    def display_reverse(self):
        stack = []
        current = self.head

        while current:
            stack.append(current.data)
            current = current.next

        while stack:
            print(stack.pop(), end=" -> ")
        print("None")

if __name__ == "__main__":
    linked_list = LinkedList()

    # Create a list
    elements = [5, 2, 9, 1, 5, 6]
    for element in elements:
        linked_list.append(element)

    # Find the smallest element
    smallest = linked_list.find_smallest()
    print("Smallest element:", smallest)

    # Insert an element if not a duplicate
    linked_list.insert_unique(3)
    linked_list.insert_unique(6)  # Duplicate, won't be inserted

    # Display the elements in reverse order
    print("Elements in reverse order:")
    linked_list.display_reverse()


# # 7.Write a python program to implement the various operations for Stack ADT
# i.) Push ii.) Pop iii.) Display.

# In[14]:


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop.")

    def display(self):
        print("Stack:", self.items)

# Example usage:
if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()

    popped_item = stack.pop()
    print("Popped item:", popped_item)
    stack.display()


# # 8. Write a python script to implement the various operations for Queue ADT
# i.) Insert ii.) Delete in.) Display.

# In[15]:


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, item):
        self.items.append(item)

    def delete(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty. Cannot delete.")

    def display(self):
        print("Queue:", self.items)

# Example usage:
if __name__ == "__main__":
    queue = Queue()

    queue.insert(1)
    queue.insert(2)
    queue.insert(3)
    queue.display()

    deleted_item = queue.delete()
    print("Deleted item:", deleted_item)
    queue.display()


# # 9. Write a program in python to convert the following infix expression to its postfix form using push and pop operations of a Stack
# a. A/B^C+D E-FG
# b. (B^2-4°A°C) (1/2) (100)

# In[16]:


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

def infix_to_postfix(expression):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    stack = Stack()
    postfix = []
    
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == "(":
            stack.push(char)
        elif char == ")":
            while not stack.is_empty() and stack.peek() != "(":
                postfix.append(stack.pop())
            stack.pop()  # Remove the "(" from the stack
        else:
            while not stack.is_empty() and precedence.get(char, 0) <= precedence.get(stack.peek(), 0):
                postfix.append(stack.pop())
            stack.push(char)
    
    while not stack.is_empty():
        postfix.append(stack.pop())
    
    return "".join(postfix)

# Example usage:
if __name__ == "__main__":
    infix1 = "A/B^C+D"
    infix2 = "(B^2-4*A*C)*(1/2)*(100)"
    
    postfix1 = infix_to_postfix(infix1)
    postfix2 = infix_to_postfix(infix2)
    
    print("Infix 1:", infix1)
    print("Postfix 1:", postfix1)
    
    print("Infix 2:", infix2)
    print("Postfix 2:", postfix2)


# In[ ]:




