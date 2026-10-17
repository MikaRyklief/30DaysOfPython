# Exercise Day - 3

# Question 1, 2, 3 - 
# Declare your age as integer variable
# Declare your height as a float variable
# Declare a variable that store a complex number
age = 22
height = 1.80
var = 8 + 7j

# Question 4 - Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
b = int(input("Enter base: "))
h = int(input("Enter height: "))

area = 0.5 * b * h

print("The area of the triangle is", area, "\n")

# Question 5 - Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = int(input("Enter side a: "))
side_b = int(input("Enter side b: "))
side_c = int(input("Enter side c: "))

perimeter = side_a + side_b + side_c

print("The perimeter of the triangle is", perimeter, "\n")

# Question 6 - Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Enter length of rectangle:"))
width = int(input("Enter width of rectangle:"))

area = length * width
perimeter = 2 * (length + width)

print("The area of the rectangle is", area)
print("The perimeter of the rectangle is", perimeter, "\n")

# Question 7 - Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
import math

r = int(input("Enter radius of circle: "))

area = math.pi * r **2
circumference = 2 * math.pi * r

print("The area of the circle is", int(area), "and the circumference is", int(circumference), "\n")

# Question 8 - Calculate the slope, x-intercept and y-intercept of y = 2x -2

m = 2
c = -2

slope1 = m

y_intercept = (0, c)
x_intercept = (int(-c / m), 0)

print("The slope is:", m)
print("The y intercept is:", y_intercept)
print("The x intercept is:", x_intercept, "\n")

# Question 9 - Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
y2 = 10
y1 = 2
x2 = 6
x1 = 2
m = (y2 - y1) / (x2 - x1)

slope2 = m

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("The slope is", round(slope2, 2), "and the euclidean distance is", round(distance, 2), "\n")

# Question 10 - Compare the slopes in tasks 8 and 9.

print(slope1 > slope2)
print(slope1 < slope2)
print(slope1 == slope2)
print(slope1 != slope2)
print(slope1 >= slope2)
print(slope1 <= slope2, "\n")

# Question 11 - Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = 0
y = x**2 + (6*x) + 9
print('The value of Y is:', y)

x = -1 
y = x**2 + (6*x) + 9
print('The value of Y is:', y)

x = -2
y = x**2 + (6*x) + 9
print('The value of Y is:', y)

x = -3
y = x**2 + (6*x) + 9
print('The value of Y is:', y, ', So the value of X is -3')

# Question 12 - Find the length of 'python' and 'dragon' and make a falsy comparison statement.

len("python") < len("dragon") # You have to separate the strings as if you did len('python' < 'dragon'), it would check which word comes first alphabetically and give a boolean value which cannot work in len.

# Question 13 - Use and operator to check if 'on' is found in both 'python' and 'dragon'

print('on' in 'python' and 'on' in 'dragon')

# Question 14 - I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print('jargon' in 'I hope this course is not full of jargon.')

# Question 15 - There is no 'on' in both dragon and python

print('on' not in 'python' and 'on' not in 'dragon')

# Question 16 - Find the length of the text python and convert the value to float and convert it to string

float(len('python'))
str(len('python'))

# Question 17 - Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

x % 2 == 0 

# Question 18 - Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

print(7//3 == int(2.7))

# Question 19 - Check if type of '10' is equal to type of 10

print(type('10') == type(10))

# Question 20 - Check if int('9.8') is equal to 10

print(int(9.8) == 10)

# Question 21 - Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))

earning = hours * rate 

print("Your weekly earning is R", earning)

# Question 22 - Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

years = int(input("Enter number of years you have lived: "))

seconds = years * 60 * 60 * 24 * 365

print("You have lived for", seconds, "seconds")

# Question 23 - Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

print('1 1 1 1 1' '\n' 
      '2 1 2 4 8' '\n'
      '3 1 3 9 27' '\n'
      '4 1 4 16 64' '\n'
      '5 1 5 25 125')