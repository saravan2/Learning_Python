import random

feet_in_mile = 5280
meters_in_kilomeeter = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"]

def roll_dice(num):
    return random.randint(1, num)

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]