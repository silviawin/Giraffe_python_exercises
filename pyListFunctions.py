lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim",  "Oscar", "Tobi"]
# friends.extend(lucky_numbers)
friends.append("Lia")
friends.insert(1, "Kelly")
# friends.remove("Jim")
# clear entire list
# friends.clear()
# pop removes the last element
friends.pop()
print(friends)
print(friends.index("Kevin"))
print(friends.count("Jim"))
friends.sort()
lucky_numbers.sort()
print(friends)
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)