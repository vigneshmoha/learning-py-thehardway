my_name = "Mohan Annasamy"
my_age = 27
my_height = 172 # in centimeters
my_weight = 68 # in kilograms
my_eyes = "black"
my_teeth = "white"
my_hair = "black"

print(f"Let's talk about {my_name}.")
print(f"He is {my_height} centimeters tall.")
print(f"He is {my_weight} kilograms heavy.")
print(f"Actually he is not too heavy.. Perfect weight per se.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the candy.")

# Following line involves some maths..

#centimeterToMeter
my_height_in_meter = my_height / 100
BMI = my_weight / ((my_height_in_meter) * (my_height_in_meter))

print(f"His BMI is {BMI}")