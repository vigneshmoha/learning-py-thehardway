print("Let's practice everything i learned so far..")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\t The lovely world 
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere is none.
"""

print("-------------------------------")
print(poem)
print("-------------------------------")

five = 10 - 2 + 3 - 6
print(f"Answer must be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

# Do you remember that there is another way to format the string?
print("With a starting point of {}".format(start_point))

# Above is same as f"" string
print(f"We'd have {beans} beans, {jars} jars and {crates} crates.")

start_point = start_point / 10

print(f"We can also do this way with new starting point {start_point}")
formula = secret_formula(start_point)

# This is an easy way to apply a list to a format string --> :) Best idea but not sure how it affects the performance
print("We'd have {} beans, {} jars and {} crates".format(*formula))