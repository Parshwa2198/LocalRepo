



str1=("hello world")
str2='prime'
word="prinme"
print(len(word))
#lenth function is built in function and we can use to print lentght of strings
#concanete can we also used to add two strings togather with help pf + operator
word=str1+""+str2
print(word)
#loop on strings
s="python"
for ch in s:
    print(ch)
#index in as sequence represnts the positon value of individula eletes
s = "Python"
print(s[0]) #'p"
print(s[3]) # 'h'
print(s[-1]) # 'n'
#Slicing in strings
#Slicing is a powerful features of python that lets us access multiple elemts at onceregistry
#we can do slicing in strings and even on other sequencs like list and tupples
# define the string
s = "Python"

print(s[0:2])    # 'Py'
print(s[2:])     # 'thon'
print(s[:3])     # 'Pyt'
print(s[::2])    # 'Pto'  (every second character)
print(s[::-1])   # 'nohtyP' (reversed string)
#stings formatin
# String Indexing
s = "Python"
print(s[0])     # 'P'
print(s[3])     # 'h'
print(s[-1])    # 'n'

# String Slicing
s = "Python"
print(s[0:2])   # 'Py'
print(s[2:])    # 'thon'
print(s[:3])    # 'Pyt'
print(s[::2])   # 'Pto'
print(s[::-1])  # 'nohtyP'

# Using format()
name = "Rahul"
age = 25
print("My name is {} and I am {} years old".format(name, age))

print("Coordinates: {1}, {0}".format("x", "y"))
print("Name: {n}, Age: {a}".format(n="Bob", a=30))

# Using f-strings
name = "Rahul"
age = 25
print(f"My name is {name} and I am {age} years old.")

# List examples
my_list = [1, 2, 3, "apple", 3.14, [10, 20]]
print(my_list)
print(my_list[0])      # first element
print(my_list[-1])     # last element
print(my_list[3])      # 'apple'
print(my_list[5][1])   # 20
a=5
b=10
print(f"sumof{a}&{b}={a+b}")
print(f"avgof{a}&{b}={(a+b)/2}")
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list)) # <class 'list'>
my_list2=[10,"Hello",3.14,True,10]#heterogenouslistprint(my_list2)
print(my_list2)
my_list=[1,2,3,4,5]
print(my_list)
print(type(my_list))
my_list2=[10,"Hello",3.14,True,10]
print(my_list2)

numbers = [0,1,2,3,4,5,6,7,8,9]

# Simple Slice
print(numbers[2:5])      # [2, 3, 4]
print(numbers[:4])       # [0, 1, 2, 3]
print(numbers[5:])       # [5, 6, 7, 8, 9]
print(numbers[:])        # [0,1,2,3,4,5,6,7,8,9]

# Using STEP
print(numbers[::2])      # [0, 2, 4, 6, 8]
print(numbers[1::3])     # [1, 4, 7]

# Negative slice
print(numbers[-5:-2])    # [5, 6, 7]

nums = [5, 2, 9]
print(len(nums))         # 3

nums.append(7)
print(nums)              # [5, 2, 9, 7]

nums.insert(1, 4)
print(nums)              # [5, 4, 2, 9, 7]

nums.sort()
print(nums)              # [2, 4, 5, 7, 9]

nums.reverse()
print(nums)              # [9, 7, 5, 4, 2]


#python is an ordered ,immutable collection of items.
#examples
tup=(10,10,30)
print(tup)
print(type(tup))
empty_tu_ple=()
single_element_tuple=(42,)
s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]

average = sum(numbers) / len(numbers)

print("Average:", average)
# Input two lists of integers
list1 = [int(x) for x in input("Enter list 1 numbers: ").split()]
list2 = [int(x) for x in input("Enter list 2 numbers: ").split()]

# Merge both lists
result = list1 + list2

# Sort the merged list
result.sort()

print("Merged and Sorted List:", result)
# Input a tuple of integers from the user
t = tuple(int(x) for x in input("Enter tuple numbers: ").split())

# Create tuple of even numbers
even_tuple = tuple(x for x in t if x % 2 == 0)

# Create tuple of odd numbers
odd_tuple = tuple(x for x in t if x % 2 != 0)

print("Even numbers tuple:", even_tuple)
print("Odd numbers tuple:", odd_tuple)
# Initialize empty dictionary
students = {}

while True:
    print("\nMenu:")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("E - Exit")

    choice = input("Enter your choice: ").upper()

    if choice == "A":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print(f"{name} added successfully.")

    elif choice == "B":
        name = input("Enter student name to update marks: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print(f"{name}'s marks updated.")
        else:
            print("Student not found!")

    elif choice == "C":
        name = input("Enter student name to search: ")
        if name in students:
            print(f"{name} has marks: {students[name]}")
        else:
            print("Student not found!")

    elif choice == "D":
        print("All students and marks:")
        for name, marks in students.items():
            print(f"{name} : {marks}")

    elif choice == "E":
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Please enter A, B, C, D, or E.")
# List of words
words = ["apple", "banana", "kiwi", "cherry", "mango"]

# Create dictionary mapping word to its length
word_length = {word: len(word) for word in words}
print("Word lengths dictionary:", word_length)

# Count number of spaces in a user string
user_string = input("Enter a string: ")
space_count = user_string.count(" ")
print("Number of spaces:", space_count)
# Take input from user
user_string = input("Enter a string: ")

# Count the spaces
space_count = user_string.count(" ")

# Print the result
print("Number of spaces:", space_count)
# Input two lists

list1 = [int(x) for x in input("Enter list 1: ").split()]
list2 = [int(x) for x in input("Enter list 2: ").split()]

# Convert to sets
set1 = set(list1)
set2 = set(list2)

# Check for common elements
if set1.isdisjoint(set2):
    print("No common elements")
else:
    print("Some common elements exist")
lst = [int(x) for x in input("Enter list of numbers: ").split()]

# Using sets to find duplicates
duplicates = {x for x in lst if lst.count(x) > 1}
print("Elements appearing more than once:", duplicates)
user_string = input("Enter a string: ")

# Use set to get unique characters
unique_chars = set(user_string)

print("Unique characters:", unique_chars)
print("Count of unique characters:", len(unique_chars))
def hello():
    print("hello")
    print("from python")


hello()
#
def sum(a,b):
    sum = a + b
    return sum
sum(1, 2)

