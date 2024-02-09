import math

def sphere_volume(radius):
    if radius < 0:
        return "Radius must be non-negative."
    else:
        volume = (4/3) * math.pi * radius**3
        return volume

# Example usage:
radius = float(input())
result = sphere_volume(radius)

if type(result) == float:
    print("The volume of the sphere with radius" ,radius,"is" ,result, "cubic units.")
else:
    print(result)