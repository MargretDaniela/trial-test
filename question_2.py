import math 
#pie value
# Question 2
#Using a function create a program that calculates the volume of a cylinder.
height = float(input("Enter the height of the cylinder :"))
radius = float(input("Enter the height of the cylinder :"))
pie = math.pi
volume = pie * radius ** 2 * height
print(f"The volume of the cylinder {volume:.2f}")