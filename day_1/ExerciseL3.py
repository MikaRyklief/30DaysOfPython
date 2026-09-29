# Question 1 

print(type(55)) # Integer
print(type(3.15)) # Float
print(type(5 + 88j)) # Complex number
print(type("Mika")) # String
print(type(False)) # Boolean
print(type(['South Africa', 'America', 'Chile'])) # List
print(type((9.6, 76.5, 778,332))) # Tuple
print(type({9.7, 4565, 47.45})) # Set
print(type({'name' : 'Mika'})) # Dictionary

# Question 2
import math # Importing math function to use PI

x1 = 2 # Declared x1 
x2 = 10 # Declared x2

y1 = 3 # Declared y1
y2 = 8 # Declared y2

d = (x2 - x1)**2 + (y2 - y1)**2 # Calculation to find the distance between two points/co-ordinates

distance = math.sqrt(d) # Used the square root function to calculate the distance and declared distance to the square root of d

print(distance) 
