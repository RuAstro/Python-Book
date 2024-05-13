#tuples_exercise
cardinal_numbers = ("first", "second", "third")
print(cardinal_numbers[1])

cardinal_numbers = "position1", "position2", "position3"
print("position1")
print("position2")
print("position3")

my_name = tuple("Ruan")

"x" in my_name

print(my_name[1:])   #slicing





#Nesting, Copying, and Sorting Tuples and Lists
data = ((1, 2), (3, 4))

index = 1
for row in data:
    print(f"Row {index} sum: {sum}(row)")
    index += 1
    
    numbers = [4, 3, 2, 1]
    numbers_copy = numbers[:]
    
    numbers.sort()
    print(numbers)
    
    
    
    
# 9.6 - Store Relationships in Dictionaries
captains = {}

captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

if "Enterprise" not in captains:
    captains["Enterprise"] = "unknown"
    
if  "Discovery" not in captains:
    captains["Discovery"] = "unknown"
    
for ship, captain in captains.items():
    print("The {ship} is captained by {captains}.") 
    
del captains["Discovery"]

captains = dict(
    [
        ("Enterprise", "Picard"),
        ("Voyager", "Janeway"), 
        ("Defiant", "Sisko"),
    ]
)