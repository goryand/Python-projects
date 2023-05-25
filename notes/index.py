print("Hello World!")

print("Good morning.")
# name = input("What is your name?\n")
# print("Hello, " + name + "!")


Fruits = ["Apple", "Orange", "Peach", "Candy"]
Fruits.append("Mango")
Fruits.remove("Candy")  # or: del Fruits[4]
print(Fruits)

List = [1, 2, 3, 4, 5, 6]
if 1 in List:
    print("1 is in the list!")
ListTotal = sum(List)
print("ListTotal: " + str(ListTotal))

if "Apple" in Fruits:
    print("I love apples!")
else:
    print("I miss apples!")

for iFruit in Fruits:
    print("Fruit iterated: " + iFruit)

range(7)  # -> [0,1,2,3,4,5,6]

tasteLog = {
    "Big Mac": "very tasty",
    "Broccoli": "tasty"
}

tasteLog["McNuggets"] = "very tasty"
tasteLog["Coca Cola"] = "Godlike tasty"

# Broccoli sucks, lets delete it
# i am laughing to myself doing this at may 25 2023 1:56 AM
del tasteLog["Broccoli"]

# I forgot if I added Candy to the list, but dont want an error. I will utilize .get
candyTaste = tasteLog.get("Candy")
print(candyTaste)
# -> returns 'None', which is nil or null



