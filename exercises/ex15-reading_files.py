from sys import argv

script, filepath = argv

#open the file in the respective path
txt = open(filepath)

print(f"Here is your file {filepath}")
#Read the file content
print(txt.read())
txt.close()

print("Type the filepath again:")
file_again = input("> ")

#open the file in the respective path
txt_again = open(file_again)
#Read the file content
print(txt_again.read())
txt_again.close()