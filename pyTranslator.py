# make all the vowels become "g"

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g "
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

# if letter.lower in "aeiou"
# only have to type out the lower case letters

