from math import *
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")
character_name = "John"
character_age = "35"
print("There was once a man named " + character_name + ",")
print("he was " + character_age + " years old. ")
character_name = "Mike"
character_age = "50"
print("He really like the name " + character_name + ", ")
print("but he did not like being " + character_age + ".")
print("Giraffe\\Academy")
phrase = "Giraffe Academy"
print("Phrase : ", phrase)
'''
upper case upper()
is upper case ? isupper()
length via len
index of string via [index]
'''
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[3])
print("phrase.index(\"a\") : ", phrase.index("a"))
print(phrase.replace("Giraffe", "Elephant"))
print(phrase)
'''
Order of operations
'''
print(2.0987 + 6)
print(3 * (4 + 5))
my_num = -5
'''
math functions
integer to string conversions
'''
print(my_num)
print(str(my_num) + " is my favorite number.")
print(abs(my_num))
print(min(4, my_num))
print(floor(4.3))
print(ceil(4.3))
print(sqrt(36))

'''
input() to get user input
'''

'''
red
name = input("Enter your name : ")
age = input ("Enter your age : ")
print("Hello " + name + "! You are " + age)

num1 = input("Enter your number : ")
num2 = input("Enter another number : ")
result = float(num1) + float(num2)
print(result)


color =  input("Enter a color: ")
plural_noun =  input("Enter a plural noun: ")
celebrity =  input("Enter a color: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
'''

'''
Lists
'''
friends = ["Kevin", "Karen",  "Jim"]
print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])
friends[1] = "Mike"
print(friends[1:3])
lucky_numbers = [4, 8, 9, 7, 56, 23]

'''
List functions
'''
#friends.extend(lucky_numbers)
#friends.append("Creed")
#friends.insert(1, "Kelly")
#friends.remove("Jim")
#friends.clear()
#friends.pop()
# Index finds the first instance of key
print(friends.index("Kevin"))
friends.append("Kevin")
print(friends.index("Kevin"))
print(friends.count("Kevin"))
# If key is not in list, we would have an error
#print(friends.index("Saravana"))
friends.sort()
lucky_numbers.sort()
print(friends)
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)

'''
Tuples () are immutable
Lists [] are mutable
'''
coordinates = (4, 5)
print(coordinates)
#coordinates[1] = 10
print(coordinates[0], coordinates[1])
coordinates1 = [(4,5), (6,5)]
print(coordinates1)
coordinates1[1] = (17, 8)
print(coordinates1)
print(coordinates1[1][1])

'''
Functions
'''
def say_hi():
    print("Hi")

say_hi()

def cube(num):
    return (num * num * num)

result = cube(3)
print(result)

'''
Boolean
'''
is_male = True
is_tall = False

'''
if
elif
else

We cannot use !boolean variable
'''
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a shirt male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")

def max_num(num1, num2, num3):
    # != <= also exists
    # Strings can also be used
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,4,5))

'''
Dictionaries
'''

monthConversions = {
    "Jan" : "January",
    "Dec" : "December",
    5 : "May"
}

print(monthConversions["Jan"])
# Key error if key doesnot exist
#print(monthConversions["Feb"])
print(monthConversions.get("Dec"))
# No key get results in None
print(monthConversions.get("Feb"))
# We can specify error string / default value when get fails
print(monthConversions.get("Feb", "SAR"))
print(monthConversions.get(5, "SAR"))

'''
While loop
'''
i = 1
while i <= 10:
    print(i)
    i = i + 1

print("Done with loop")

'''
For loop
'''

for letter in "Giraffe Academy":
    print(letter)

friends3 = ["Jim", "Kevin", "Kelly"]
for name in friends3:
    print(name)

for index in range(10):
    print(index)

for index in range(3, 10):
    print(index)

#length of list via len(list)
for index in range(len(friends3)):
    print(friends3[index])

for index in range(10):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")

'''
Exponent function
'''
print(2**3)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 3))

'''
2D lists
'''

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[0])
print(number_grid[0][0])

for row in number_grid:
    print(row)

'''
Nested for loop
'''

for row in number_grid:
    for col in row:
        print(col)

def translate(phrase):
    translation = ""
    for letter in phrase:
        #if letter in "AEIOUaeiou":
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate("Oog"))

# Convention is to use # for even multi line python

'''
Catching errors
'''

try:
    value = 10 / 0
    number = int("asdf")
    print(number)
#except: Too broad
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid integer")

'''
Files
'''

# Modes are r, w, a, r+
employee_file = open("employees.txt", "r")
print(employee_file.readable())
#print(employee_file.read())
#print(employee_file.readline())
#print(employee_file.readline())
#print(employee_file.readlines())
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

employee_file = open("employees.txt", "a")
print(employee_file.readable())
employee_file.write("\nToby - HR")
employee_file.close()

html_file = open("index.html", "w")
html_file.write("<p>This is HTML</p>")
html_file.close()

'''
Modules in python
Python module index

Built in modules
External modules

Pycharm uses Python3 and has pip installed
Mac OS has older Python 2.7 installed with no pip

We can use the pycharm terminal to install modules.


pip install <external module>
installed in <Python 3.7 (Project name)>/site-packages/ in pycharm

pip uninstall <external module>

import <file name>
'''

import useful_tools
print(useful_tools.roll_dice(4))
print(useful_tools.get_file_ext("app.py"))

'''
Classes and Objects
Class is your own datatype
Model real world objects
'''
from Student import Student
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student1.gpa)
print(student2.major)
print(student1.on_honor_roll())

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n"
]

from Question import Question
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

# run_test(questions)

'''
Inheritence
'''
from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_salad()
myChef.make_chicken()

myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_salad()

'''
Interpreter

We can use it as a scratchpad to test stub code

Open terminal and type python3

>>> def say_hi(name):
...     print("Hello " + name)
... 
>>> say_hi("Mike")
Hello Mike

'''