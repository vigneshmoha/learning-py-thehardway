# This one is like argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# *args is pointless, we can just do this.
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# It takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

def print_nothing():
    print("You know nothing JON SNOW!")

print_two("Mohan", "Annasamy")
print_two_again("Mohan", "Annasamy")
print_one("Mohan Annasamy")
print_nothing()