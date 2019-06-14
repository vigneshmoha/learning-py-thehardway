from sys import argv

script, input_file = argv

def print_all_content(file_object):
    print(file_object.read())

def rewind(file_object):
    file_object.seek(0)

def print_a_line(line_count, file_object):
    print(line_count, file_object.readline())

current_file = open(input_file)

print("Let's print the whole file first..")
print_all_content(current_file)

print("Let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")
line_no = 1

print_a_line(line_no, current_file)
line_no = line_no + 1
print_a_line(line_no, current_file)
line_no = line_no + 1
print_a_line(line_no, current_file)

current_file.close()