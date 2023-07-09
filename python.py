print("Hello from inside a file!")

def hello():
    print("Hello user!")

hello()

# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.
def pack(arg1, arg2, arg3):

    return[arg1, arg2, arg3]

print(pack("Hello", 10, False))

# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that 
# say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). 
# If the list is empty, print "My lunchbox is empty!". The function should not return anything
food_list= ["Steak", "Potatos", "Broccoli"]

def eat_lunch(food_list):
    if len(food_list) == 0:
        print("My lunch is empty")
    else:
        print("First I eat", food_list[0]) # Slicing method starts from the second index. Must have this to print first index.
        for food in food_list[1:]:         # Slice through whole list and print them in next line.
            print("Next I eat", food)

food_list = ["Steak", "Potatos", "Broccoli"]
eat_lunch(food_list)