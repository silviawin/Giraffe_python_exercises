# for loop is to loop through different collections of items
# ex: different arrays or the letters inside a string

friends = ["jim", "ana", "mario", "carla", "dani"]

for letter in "Giraffe Academy":
    print(letter)

print("\n")

for friend in friends:
    print(friend)

print("\n")

for index in range(10):
    print(index)

print("\n")

for elemento in range(3,10):
    print(elemento)

print("\n")

for index in range(len(friends)):
    print(index)
    print(friends[index])

print("\n")

for index in range(len(friends)):
    print(friends[1])

print("\n")

for especial in range(5):
    if especial == 0:
        print("First Iteration")
    else:
        print("More numbers are cool")



