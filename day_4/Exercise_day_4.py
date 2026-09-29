# Exercise Day - 4

# Question 1 - Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

word = ['Thirty', 'Days', 'Of', 'Python']

print(' '.join(word)) # Using the .join() method to concatenate a List of strings.

# Question 2 - Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

first_word = 'Coding'
second_word = 'For'
third_word = 'ALL'
space = ' '

full_word = first_word + space + second_word + space + third_word # Using a different approach (+) to concatenate the strings. 
print(full_word)

# Question 3 - Declare a variable named company and assign it to an initial value "Coding For All".
# Question 4 - Print the variable company using print().

company = "Coding For All"
print(company)

# Question 5 - Print the length of the company string using len() method and print().
print(len(company))

# Question 6 - Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Question 7 - Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Question 8 - Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize() + '\n' + company.title() + '\n' + company.swapcase())

# Question 9 - Cut(slice) out the first word of Coding For All string.
first_word = company[0:6] # Sliced the first word from "Coding For All" and printed it.
print(first_word)

# Question 10 - Check if Coding For All string contains a word Coding using the method index, find or other methods.
sub_string = "Coding"

print(company.find('Coding'))
print(company.index(sub_string))

# Question 11 - Replace the word coding in the string 'Coding For All' to Python.

print(company.replace("Coding", "Python"))

# Question 12 - Change "Python for Everyone" to "Python for All" using the replace method or other methods.

result = "Python for Everyone"

print(result.replace("Everyone", "All"))

# Question 13 - Split the string 'Coding For All' using space as the separator (split()) .

print(company.split())

# Question 14 - "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

jobs = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(jobs.split(","))

# Question 15 - What is the character at index 0 in the string Coding For All.

print(company[0])

# Question 16 - What is the last index of the string Coding For All.

last_index = len(company) - 1
print(last_index)

# Question 17 - What character is at index 10 in "Coding For All" string.

print(company[10])

# Question 18 - Create an acronym or an abbreviation for the name 'Python For Everyone'.

challenge = 'Python For Everyone'
acronym = challenge[0] + challenge[7] + challenge[11] # Created a variable 'acronym' and used indexing to get a character of each word in the string.
print(acronym)

# Question 19 - Create an acronym or an abbreviation for the name 'Coding For All'.

abbr = company.split() # Used the .split() method to split our variable company into a list and assigned it to variable abbr.
print(abbr[0][0] + abbr[1][0] + abbr[2][0]) # Used indexing to first get the word i need in the list and then used index to get character of that word.

# Question 20 - Use index to determine the position of the first occurrence of C in Coding For All.

substring = 'C'
print(company.index(substring))

# Question 21 - Use index to determine the position of the first occurrence of F in Coding For All.

substring = 'F'
print(company.index(substring))

# Question 22 - Use rfind to determine the position of the last occurrence of l in Coding For All People.

substring = 'l'
print(company.rindex(substring))

# Question 23 - Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

words = 'You cannot end a sentence with because because because is a conjunction'
print(words.find('because'))

substring = 'because'
print(words.index(substring))

# Question 24 - Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(words.rindex('because'))

# Question 25 - Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

slicing = words[31:54]
print(slicing)

# Question 26 - Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(words.index('because'))

# Question 27 - Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

slicing = words[31:54]
print(slicing)

# Question 28 - Does 'Coding For All' start with a substring Coding?
# print(company.startswith("Coding")) - Simpler way using the .startswith() method 

company = 'Coding For All'

a = company.split()
print(a[0] == 'Coding')

# Question 29 - Does 'Coding For All' end with a substring coding?

print(company.endswith("coding"))

# Question 30 - '   Coding For All      '  , remove the left and right trailing spaces in the given string.

company2 = '   Coding For All      '
print(company2.strip())

# Question 31 - Which one of the following variables return True when we use the method isidentifier():
# - 30DaysOfPython
# - thirty_days_of_python

a = '30DaysOfPython'
b = 'thirty_days_of_python'

print(a.isidentifier())
print(b.isidentifier()) # Answer is 'thirty_days_of_python'

# Question 32 - The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

names = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

print('# '.join(names))

# Question 33 - Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.

print("I am enjoying this challenge.\nI just wonder what is next.")

# Question 34 - Use a tab escape sequence to write the following lines. 
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki

print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki'.expandtabs(10))

# Question 35 - Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

radius = 10 
area = int(3.14*radius**2)
print('The area of a circle with radius {} is {} meters square.'.format(radius, area))

# Question 36 - Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
