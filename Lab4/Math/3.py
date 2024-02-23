import math

# Get input from the user
num_sides = int(input("Number of sides: "))
side_length = float(input("The length of a side: "))

# Calculate the area of the regular polygon
area = (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))

# Print the result
print(f"The area of the polygon is: {area}")