#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1 Write a python function that copies a file reading and writing upto 50 characters at a time.


# In[2]:


def copy_f():
    with open('python','r') as first:
        dc=first.read(50)
    with open('python new','w') as second:
        second.write(dc)
    
    with open('python new','r') as second:
        result=second.read()
        print(result)

copy_f()




# In[ ]:


2 Print all numbers present in the text file and print the number of blank spaces in that file.


# In[3]:


source_file_path =  ('python')
def program(source_file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            numbers = []
            spaces_count = 0
            
            for character in text:
                if character.isdigit():
                    numbers.append(character)
                elif character.isspace():
                    spaces_count += 1
            numbers_str = ''.join(numbers)
            print("Numbers in the file:", numbers_str)
            print("Number of blank spaces:", spaces_count)
    
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
file_path = 'python'  
program(file_path)


# In[ ]:


3 Write a function called sed that takes as arguments a pattern.........


# In[4]:


def sed(pattern, replacement, input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, 'r') as infile:
            # Read the contents of the input file
            file_contents = infile.read()

        # Replace the pattern with the replacement string
        modified_contents = file_contents.replace(pattern, replacement)

        # Open the output file for writing
        with open(output_file, 'w') as outfile:
            # Write the modified contents to the output file
            outfile.write(modified_contents)

    except FileNotFoundError:
        print(f"Error: One or both of the specified files not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    else:
        print(f"File '{input_file}' processed successfully. Output written to '{output_file}'.")

sed("old_text", "new_text", "python", "python new")
f=open("python new",'r')
f.read()


# In[ ]:


5a write a python code to search for and replace text within a text file


# In[5]:


def search_Text(input_file, output_file, search_text, replace_text):
    
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                # Replace occurrences of search_text with replace_text in each line
                modified_line = line.replace(search_text, replace_text)
                outfile.write(modified_line)
        print("Replacement complete. Check {} for the updated content".format(output_file))


search_text = "old_word"
replace_text = "new_word"
input_file = "python"
output_file = "python new"

search_Text("python", "python new", 'in', 'the')

f=open("python new","r")
f.read()


# In[ ]:


6 Function to concatenate multiple text files into a single output file


# In[ ]:


def concatenate_text_files(input_files, output_file):
    try:
        with open(output_file, 'w') as output:
            for input_file in input_files:
                with open(input_file, 'r') as file:
                    output.write(file.read() + "\n")
        print(f"Successfully concatenated {len(input_files)} files into {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Input files and output file paths
input_files = []
while True:
    file_path = input("Enter the path of an input text file (or 'done' to finish): ")
    if file_path.lower() == 'done':
        break
    input_files.append(file_path)

output_file = input("Enter the path of the output text file: ")

# Concatenate the input files into the output file
concatenate_text_files(python,destination)
f=open("destination","r")
f.read()


# In[ ]:


7


# In[ ]:


# Define the input and output file names
input_file_name = 'python'
output_file_name = 'python new'

try:
    # Step 1: Open input.txt for reading
    with open(input_file_name, 'r') as input_file:
        word_length_dict = {}  # Step 2: Create an empty dictionary

        # Step 3: Loop through each line in the input file
        for line in input_file:
            word = line.strip()  # Step 4: Strip leading/trailing whitespace
            length = len(word)   # Calculate the length of the word

            # Step 5: Add the word and its length to the dictionary
            word_length_dict[word] = length

    # Step 6: Open output.txt for writing
    with open(output_file_name, 'w') as output_file:
        # Step 7: Write the word-length dictionary to the output file
        for word, length in word_length_dict.items():
            output_file.write(f"{word}: {length}\n")

    print("Processing completed. Check 'output.txt' for results.")

except FileNotFoundError:
    print(f"Error: {input_file_name} not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")


# In[ ]:


8


# In[ ]:


import os

# Function to input and store student grades for a subject
def input_grades(subject):
    try:
        file_name = f"{subject}.txt"
        with open(file_name, "a") as file:
            student_name = input("Enter student name: ")
            grade = input(f"Enter {subject} grade for {student_name}: ")
            file.write(f"{student_name}: {grade}\n")
        print(f"Grade for {student_name} in {subject} has been recorded.")
    except IOError as e:
        print(f"Error: {e}")

# Function to view student grades for a subject
def view_grades(subject):
    try:
        file_name = f"{subject}.txt"
        if not os.path.exists(file_name):
            print(f"No grades recorded for {subject} yet.")
            return

        with open(file_name, "r") as file:
            print(f"Grades for {subject}:")
            for line in file:
                print(line.strip())
    except IOError as e:
        print(f"Error: {e}")

# Main program loop
while True:
    print("\nStudent Gradebook System")
    print("1. Input Grades")
    print("2. View Grades")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        subject = input("Enter the subject: ")
        input_grades(subject)
    elif choice == "2":
        subject = input("Enter the subject: ")
        view_grades(subject)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print("Goodbye!")


# In[ ]:




