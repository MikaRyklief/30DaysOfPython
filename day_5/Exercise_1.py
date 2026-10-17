# Exercise Day - 5

# Question 1 - Declare an empty list

lst = []
lst1 = list()

# Question 2 - Declare a list with more than 5 items

lst = ["one", "two", "three", "four", "fifth"]

# Question 3 - Find the length of your list

print(len(lst))

# Question 4 - Get the first item, the middle item and the last item of the list

print(lst[0], lst[3], lst[len(lst) - 1])

# Question 5 - Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["Mika", 22, 1.80, "single", "28 Jungle Road"]

# Question 6 - Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Question 7 - Print the list using print()

print(mixed_data_types)
print(it_companies)

# Question 8 - Print the number of companies in the list

print(len(it_companies))

# Question 9 - Print the first, middle and last company

print(it_companies[0], it_companies[3], it_companies[len(it_companies) - 1])

# Question 10 - Print the list after modifying one of the companies

it_companies[4] = 'Hello'
print(it_companies)

# Question 11 - Add an IT company to it_companies

it_companies.insert(5,'Nvidia')
print(it_companies)

# Question 12 - Insert an IT company in the middle of the companies list

it_companies.insert(int(len(it_companies)/2), 'Mika')
print(it_companies)

# Question 13 - Change one of the it_companies names to uppercase (IBM excluded!)

it_companies[1] = it_companies[1].upper()

print(it_companies)

# Question 14 - Join the it_companies with a string '#;  '

print('#;  '.join(it_companies))

# Question 15 - Check if a certain company exists in the it_companies list.

does_exist = 'Apple' in it_companies
print(does_exist)

# Question 16 - Sort the list using sort() method

it_companies.sort()
print(it_companies)

# Question 17 - Reverse the list in descending order using reverse() method

it_companies.reverse()
print(it_companies)

# Question 18 - Slice out the first 3 companies from the list

first3 = it_companies[0:3]
print(first3)

# Question 19 - Slice out the last 3 companies from the list

last3 = it_companies[-1:-4:-1]
print(last3)

# Question 20 - Slice out the middle IT company or companies from the list

middle = it_companies[int(len(it_companies) / 2)]
print(middle)

# Question 21 - Remove the first IT company from the list

del it_companies[0]
print(it_companies)

# Question 22 - Remove the middle IT company or companies from the list

del it_companies[int(len(it_companies) / 2)]
print(it_companies)

# Question 23 - Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Question 24 - Remove all IT companies from the list

del it_companies[0:len(it_companies)]
print(it_companies)

# Question 25 - Destroy the IT companies list

del it_companies

# Question 26 - Join the following lists: Q27

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)