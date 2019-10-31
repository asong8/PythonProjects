print("Welcome to the 3D Shape Calculator!")
print("Note: All questions should be answered without capitalization or punctuation marks!")

import math

figure = ["sphere", "cylinder", "cone", "cube", "rectangular prism", "square pyramid"]

def volume():
	print("Here are the six most common 3D figures:")
	print(figure[0])
	print(figure[1])
	print(figure[2])
	print(figure[3])
	print(figure[4])
	print(figure[5])
	y = input("Which of the following figures would you like to determine the volume of?")
	while y != "sphere" and y != "cylinder" and y != "cone" and y != "cube" and y != "rectangular prism" and y != "square pyramid":
		y = input("ERROR! Please choose one of the following figures listed above: ")
	if y == "sphere":
		sphere_v()
	elif y == "cylinder":
		cylinder_v()
	elif y == "cone":
		cone_v()
	elif y == "cube":
		cube_v()
	elif y == "rectangular prism":
		prism_v()
	elif y == "square pyramid":
		pyramid_v()

def surface_area():
	print("Here are the six most common 3D figures:")
	print(figure[0])
	print(figure[1])
	print(figure[2])
	print(figure[3])
	print(figure[4])
	print(figure[5])
	z = input("Which of the following figures would you like to determine the surface area of?")
	while z != "sphere" and z != "cylinder" and z != "cone" and z != "cube" and z != "rectangular prism" and z != "square pyramid":
		z = input("ERROR! Please choose one of the following figures listed above: ")
	if z == "sphere":
		sphere_sf()
	elif z == "cylinder":
		cylinder_sf()
	elif z == "cone":
		cone_sf()
	elif z == "cube":
		cube_sf()
	elif z == "rectangular prism":
		prism_sf()
	elif z == "square pyramid":
		pyramid_sf()

def sphere_v():
	radius = float(input("Please enter the radius of the sphere: "))
	volume = (4.0/3) * math.pi * radius * radius * radius
	print("The volume of the sphere is " + str(volume))

def sphere_sf():
	radius = float(input("Please enter the radius of the sphere: "))
	SA = 4 * math.pi * radius * radius
	print("The surface area of the sphere is " + str(SA))

def cylinder_v():
	radius = float(input("Please enter the radius of the cylinder: "))
	height = float(input("Please enter the height of the cylinder: "))
	volume = math.pi * radius * radius * height
	print("The volume of the cylinder is " + str(volume))

def cylinder_sf():
	radius = float(input("Please enter the radius of the cylinder: "))
	height = float(input("Please enter the height of the cylinder: "))
	SA = (2 * math.pi * radius * height) + (2 * math.pi * radius * radius)
	print("The surface area of the cylinder is " + str(SA))

def cone_v():
	radius = float(input("Please enter the radius of the cone: "))
	height = float(input("Please enter the height of the cone: "))
	volume = (1.0/3) * math.pi * radius * radius * height
	print("The volume of the cone is " + str(volume))

def cone_sf():
	radius = float(input("Please enter the radius of the cone: "))
	height = float(input("Please enter the height of the cone: "))
	l = math.sqrt(radius * radius + height * height)
	SA = math.pi * radius * (radius + l)
	print("The surface area of the cone is " + str(SA))

def cube_v():
	length = float(input("Please enter the length of the cube: "))
	volume = length * length * length
	print("The volume of the cube is " + str(volume))

def cube_sf():
	length = float(input("Please enter the length of the cube: "))
	SA = 6 * length * length
	print("The surface area of the cube is " + str(SA))

def prism_v():
	length = float(input("Please enter the length of the rectangular prism: "))
	width = float(input("Please enter the width of the rectangular prism: "))
	height = float(input("Please enter the height of the rectangular prism: "))
	volume = length * width * height
	print("The volume of the rectangular prism is " + str(volume))

def prism_sf():
	length = float(input("Please enter the length of the rectangular prism: "))
	width = float(input("Please enter the width of the rectangular prism: "))
	height = float(input("Please enter the height of the rectangular prism: "))
	SA = 2 * ((length * width) + (width * height) + (length * height))
	print("The surface area of the rectangular prism is " + str(SA))

def pyramid_v():
	length = float(input("Please enter the length of the base of the square pyramid: "))
	height = float(input("Please enter the height of the square pyramid: "))
	volume = (1.0/3) * height * length * length
	print("The volume of the square pyramid is " + str(volume))

def pyramid_sf():
	length = float(input("Please enter the length of the base of the square pyramid: "))
	height = float(input("Please enter the height of the square pyramid: "))
	SA = (length * length) + (2 * length) * (math.sqrt(((length * length)/4) + (height * height)))
	print("The surface area of the square pyramid is " + str(SA))

x = input("Would you like to find the volume or surface area of a 3D figure? ")
while x != "volume" and x != "surface area":
	x = input("ERROR! Please choose between volume or surface area:")
if x == "volume":
	volume()
if x == "surface area":
	surface_area()

print("Thank you for using the 3D Shape Calculator!")
