print("Hello world")

# strings can be enclosed via " " or ' '
name = "ada lovelace"
# string methods
print(name.title())
print(name.upper())
# f strings, Python 3.6 and later
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
# Adding Whitespaces
print("Languages:\n\tPython\n\tC\n\tJavaScript")
favorite_language = ' python '
# Removing whitespaces
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
# String syntax errors arise because of incorrect usage of ' ' and " "
# message = 'One of Python's strengths is its diverse community.'

# Numbers
#integers, operator precedence
#spaces dont matter
print(2 + 3 * 4)
print((2 + 3) * 4)
#floats, numbers with decimal point
#Division always produces float
print(4/2)
print(2 * 0.1)

#Underscores make large numbers readable, From Python 3.6 onwards
universal_age = 14_000_000_000
print(universal_age)
print(10_00)

#Multiple Assignment
x, y, z = 0, 0.0, 0
print(x, y, f"{z}")

#Constants
MAX_CONNECTIONS = 5000
