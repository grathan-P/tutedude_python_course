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
