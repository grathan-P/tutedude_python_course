"""
Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

"""

filename="output.txt"
content1=input("Enter text to write to the file: ")

file=open(filename,"w")
writeContent=file.write(content1)
file.close()

print(f"Data succesfully written to '{filename}'.")

content2=input("Enter additional text to append: ")

file=open(filename,"a")
writeContent1=file.write("\n"+content2)
file.close()

print("Data successfully appended.")
print(f"Final content of {filename}:")

file=open(filename,"r")
readAllContent=file.read()
print(readAllContent)
file.close()