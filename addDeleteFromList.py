from viewContents import viewContents
import time
def addDeleteFromList(list_):
    displaylist = viewContents(list_)
    print(f{Currently the list looks like this: {displaylist}})
    time.sleep(2)
    addOrDelete = int(input("Would you like to 1. Add or 2. Delete - Please input either 1 or 2")).strip()
    if addOrDelete == 1:
        listContents = input("Please input the task you would like to add to the list")
        listContents = str(len(list_)+1) +"." + listContents
        priorityLevel = int(input("Please input the priority level of the task"))
        list_.append([listContents,priorityLevel])
        displaylist = viewContents(list_)
        print(f"Currently the list looks like this: {displaylist}")
    elif: addOrDelete == 2:
        foundElement = False
        elementToDelete = int(input("Enter the task number that you would like to delete"))
        for i in range(len(list_)-1):
            if list_[i][0][0] == elementToDelete:
                list_.pop(i)
                foundElement = True
            else:
                foundElement = False
        if foundElement == True:
            print("The element was successfully deleted")
        else:
            print("The element you were looking for wasn't found and hasn't been deleted")

            
