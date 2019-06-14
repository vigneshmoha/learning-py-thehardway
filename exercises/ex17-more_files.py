from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying the content from {from_file} to {to_file}")

# We could do these line in one line, how?
from_file_object = open(from_file)
from_file_data = from_file_object.read()
from_file_object.close()

print(f"The input file is {len(from_file_data)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
input("Ready? Hit ENTER to continue, CTRL+C to close..")

to_file_object = open(to_file, 'w')
to_file_object.write(from_file_data)

print("Alright, All done.")

to_file_object.close()