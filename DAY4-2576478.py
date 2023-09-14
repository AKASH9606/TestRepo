#!/usr/bin/env python
# coding: utf-8

# 1 python program with exception handling to input marks for five subjects. physics,chemistry,biology,mathematics and computer.calculate the percentage and grade according to the following
# i)percentage>=90% :grade A ii)percentage>=80% :grade B iii)percentage>=70% :grade C iv)percentage>=60% :grade D v)percentage>=40% :grade E vi)percentage<40% :grade F

# In[2]:


try:
    physics = float(input("Enter Physics marks: "))
    chemistry = float(input("Enter Chemistry marks: "))
    biology = float(input("Enter Biology marks: "))
    mathematics = float(input("Enter Mathematics marks: "))
    computer = float(input("Enter Computer marks: "))

    # Check if the marks are valid (between 0 and 100)
    if (
        0 <= physics <= 100
        and 0 <= chemistry <= 100
        and 0 <= biology <= 100
        and 0 <= mathematics <= 100
        and 0 <= computer <= 100
    ):
        total_marks = physics + chemistry + biology + mathematics + computer
        percentage = (total_marks / 500) * 100

        if percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 60:
            grade = "D"
        elif percentage >= 40:
            grade = "E"
        else:
            grade = "F"

        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")
    else:
        print("Invalid marks entered. Marks should be between 0 and 100.")

except ValueError:
    print("Invalid input. Please enter valid numerical marks.")
except Exception as e:
    print(f"An error occurred: {e}")


# 2Write a python program to input electricity unit charge and calculate the total electricity bill according to the given condition:¶
# i)For first 50 units Rs. 0.50/unit ii)For next 100 units Rs. 0.75/unit iii)For next 100 units Rs. 1.20/unit iv)For unit above 250 Rs. 1.50/unit v)An additional surcharge of 20% is added to the bill.

# In[3]:


try:
    unit_charge = float(input("Enter electricity unit charges (in kWh): "))

    # Check if the unit charge is valid (positive number)
    if unit_charge >= 0:
        if unit_charge <= 50:
            total_bill = unit_charge * 0.50
        elif unit_charge <= 150:
            total_bill = 50 * 0.50 + (unit_charge - 50) * 0.75
        elif unit_charge <= 250:
            total_bill = 50 * 0.50 + 100 * 0.75 + (unit_charge - 150) * 1.20
        else:
            total_bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (unit_charge - 250) * 1.50

        # Add a 20% surcharge
        surcharge = (total_bill * 0.20)
        total_bill += surcharge

        print(f"Total electricity bill: Rs. {total_bill:.2f}")
    else:
        print("Invalid unit charge entered. Unit charge should be a positive number.")

except ValueError:
    print("Invalid input. Please enter a valid numerical unit charge.")
except Exception as e:
    print(f"An error occurred: {e}")


# 3write a python program with exception and link to input the week number and print the weekday¶

# In[4]:


try:
    week_number = int(input("Enter a week number (1-7): "))

    # Check if the week number is valid (between 1 and 7)
    if 1 <= week_number <= 7:
        weekdays = [ "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        weekday = weekdays[week_number - 1]
        print(f"Weekday for week number {week_number}: {weekday}")
    else:
        print("Invalid week number. Week number should be between 1 and 7.")

except ValueError:
    print("Invalid input. Please enter a valid numerical week number.")
except Exception as e:
    print(f"An error occurred: {e}")


# 4

# In[ ]:


def count_words(filename):
    word_count = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip()
                if word:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
    return word_count

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python wordcount.py apple.txt")
    else:
        filename = sys.argv[1]
        word_count = count_words(filename)
        for word, count in word_count.items():
            print(f"{word}: {count}")
# command.py

import sys
from wordcount import count_words

if len(sys.argv) != 2:
    print("Usage: python command.py apple.txt")
else:
    filename = sys.argv[1]
    word_count = count_words(filename)
    for word, count in word_count.items():
        print(f"{word}: {count}")
        python command.py apple.txt


# In[ ]:


5


# In[ ]:


with open('prob5.py', 'r') as file:
    # Read the content of the file
    text = file.read()

# Convert all letters to lowercase and split the words
words = text.lower().split()

# Create a dictionary to store word frequencies
word_count = {}

# Count the frequency of each word
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Sort the words by frequency in descending order
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# Print the most frequent words
print("The most frequent words in the file are:")
for word, frequency in sorted_words[:10]:  # Change 10 to the desired number of words to display
    print(f"{word}: {frequency} times")



# In[ ]:


6


# In[ ]:


import sys

def process_text_file(input_file_path, output_file_path):
    try:
        # Check if both input and output file paths are provided
        if not input_file_path or not output_file_path:
            raise ValueError("Both input and output file paths are required.")
        
        # Check if the input file exists
        try:
            with open(input_file_path, 'r') as input_file:
                data = input_file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Input file '{input_file_path}' not found.")
        
        # Perform text processing here (you can modify 'data' as needed)
        
        # Write the processed data to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(data)
        
        print(f"File processing complete. Output written to '{output_file_path}'")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if _name_ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python program.py <input_file_path> <output_file_path>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    
    process_text_file(input_file_path, output_file_path)

