from viewContents import viewContents
from addDeleteFromList import addDeleteFromList
toDolist = [["1. Do the washing",2],["2. Do the drying",1], ["3. Fill up the car",3]]
try:
    continue_ = int(input("Welcome to the To-Do list \n There are several options you can choose from, \n 1. View the To Do list \n 2. Add/Delete from the to do list \n 3. Make changes to elements of the to do list"))
except ValueError:
    print("Please input an integer between 1-3")
if continue_ == 1:
    display = viewContents(toDolist)
    print(display)
elif continue_ == 2:
    addDeleteFromList(toDolist)
elif continue_ == 3:
    # Add a function to make changes to elements of list
    None
