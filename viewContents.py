def viewContents(toDoList):
    # List should be in format [["task"][3 <--- PRIORITY]]
    # Using concatenation there should a way to make one string that holds each of the list elements for output
    # 3 for loops that is the size of the list should allow the elements to be displayed by priority level
    displayList = ""
    for i in range(len(toDoList)):
        if toDoList[i][1] == 3:
            displayList = displayList + toDoList[i][0] + " "
    for i in range(len(toDoList)):
        if toDoList[i][1] == 2:
            displayList = displayList + toDoList[i][0] + " "
    for i in range(len(toDoList)):
        if toDoList[i][1] == 1:
            displayList = displayList + toDoList[i][0] + " "
    return displayList