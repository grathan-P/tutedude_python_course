"""
Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

"""

fileName="task1_textfile.txt"
try:
    file=open(fileName,"r")
    content=file.readlines()
    file.close()

    count=1

    print("Reading file content: ")
    for line in content:
        print(f"Line {count}: {line.strip()}")
        count+=1

except FileNotFoundError:
    print(f"Error: The file '{fileName}' was not found.")
