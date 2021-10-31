import random

feet_in_mile = 5280
meters_in_kilometer = 1000
animals = ["elephant", "giraffe", "cat", "dog"]


# to tell what the extension of the file is
def get_file_ext(filename):
    return filename[filename.index(".") + 1:]


# pass a number
def roll_dice(num):
    return random.randint(1, num)
