from sys import argv

script, filepath = argv

print(f"We are going to erase {filepath}")
print("Press ENTER to continue or CTRL+C to abort..")

input("?")

print("Opening the file..")
target = open(filepath, 'w')
print("Truncating the file. Goodbye!")
target.truncate()

print("Let's enter three lines.")
line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")

print("Program will write all the lines as a file content.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Program will close the file now.")
target.close()