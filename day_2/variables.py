# Day 2: 30 Days of python programming.

first_name = 'Mika'
last_name = 'Ryklief'
full_name = 'Mika Ryklief'
country = 'South Africa'
city = 'Cape Town'
age = 22
year = 2004
is_married = False
is_true = True
is_light_on = True
hobby, game, movie, song = 'Hockey', 'Fifa26', 'Spiderman', 'Angel'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(hobby))
print(type(game))
print(type(movie))
print(type(song))

print(len(first_name))
print((len(first_name)) - (len(last_name)) )

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

from math import pi

r = 30 
area_of_circle = pi * r**2
print('Area of Circle:', area_of_circle)

circum_of_circle = 2*pi*r
print('Circumference of Circle:', circum_of_circle)

radius = input('Please enter a radius:')
r = int(radius) # Must change user input (String) to an integer.
area = pi * r**2
print('Area of your circle is:', area)

first_name = input('Please enter your first name: ')
last_namne = input('Please enter your last name: ')
country = input('Please enter your country: ')
age = input('Please enter your age: ')
