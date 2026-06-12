# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HELPER FUNCTIONS AND IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def loadList():
    try:
        with open("savedList.txt", "r") as file:
            listIn = file.readlines()
        for idx in range(len(listIn)):
            listIn[idx] = listIn[idx].strip("\n")
    except FileNotFoundError:
        listIn = []
    finally:
        return listIn


def saveList(listIn):
    with open("savedList.txt", "w") as newSave:
        for idx in range(len(listIn)):
            if idx != len(listIn) - 1:
                newSave.write(f"{listIn[idx]}\n")
            else:
                newSave.write(listIn[idx])


def displayList(listIn):
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print("                    USER LIST 1")
    print("")
    for idx in range(len(listIn)):
        print(f"                    {idx+1}. {listIn[idx]}")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")


def addItems(listIn):
    addingItems = True
    currentList = listIn
    displayList(currentList)

    while addingItems:
        print("")
        print("Enter an item to add:")
        toAdd = input(" --> ")
        currentList.append(toAdd)

        displayList(currentList)

        validResp = False
        while not validResp:
            print("")
            print("Add another item? (y/n)")
            resp = input(" --> ").lower()

            if resp in ["y", "yes"]:
                validResp = True
            elif resp in ["n", "no"]:
                validResp = True
                addingItems = False
            else:
                print("")
                print("Invalid response - please try again.")

    saveList(currentList)


def removeItems(listIn):
    removingItems = True
    currentList = listIn
    displayList(currentList)

    while removingItems:
        validResponse = False
        while not validResponse:
            indices = [str(x) for x in range(1, len(currentList) + 1)]
            print("")
            print("Enter an item or position to remove:")
            toRemove = input(" --> ")

            if toRemove in currentList:
                currentList.remove(toRemove)
                validResponse = True
            elif toRemove in indices:
                toRemove = int(toRemove) - 1
                currentList.pop(toRemove)
                validResponse = True
            else:
                print("")
                print("Invalid choice - please try again.")
                displayList(currentList)

        displayList(currentList)

        validResp = False
        while not validResp:
            print("")
            print("Remove another item? (y/n)")
            resp = input(" --> ").lower()

            if resp in ["y", "yes"]:
                validResp = True
            elif resp in ["n", "no"]:
                validResp = True
                removingItems = False
            else:
                print("")
                print("Invalid response - please try again.")

        saveList(currentList)                


def editItems(listIn):
    editingItems = True
    currentList = listIn
    displayList(currentList)

    while editingItems:
        validResponse = False
        while not validResponse:
            indices = [str(x) for x in range(1, len(currentList) + 1)]
            print("")
            print("Enter an item or position to edit:")
            toEdit = input(" --> ")           

            if toEdit in currentList:
                editIdx = currentList.index(toEdit)
                validResponse = True
            elif toEdit in indices:
                editIdx = int(toEdit) - 1
                validResponse = True
            else:
                print("")
                print("Invalid choice - please try again.")
                displayList(currentList)

        print("")
        print("Enter the updated entry:")
        updatedEntry = input(" --> ")

        currentList[editIdx] = updatedEntry

        displayList(currentList)

        validResp = False
        while not validResp:
            print("")
            print("Edit another item? (y/n)")
            resp = input(" --> ").lower()

            if resp in ["y", "yes"]:
                validResp = True
            elif resp in ["n", "no"]:
                validResp = True
                editingItems = False
            else:
                print("")
                print("Invalid response - please try again.")

        saveList(currentList)



def moveItems(listIn):
    movingItems = True
    currentList = listIn
    displayList(currentList)

    while movingItems:
        validResponse = False
        while not validResponse:
            indices = [str(x) for x in range(1, len(currentList) + 1)]
            print("")
            print("Enter an item or position to move:")
            toMoveFrom = input(" --> ")           

            if toMoveFrom in currentList:
                fromIdx = currentList.index(toMoveFrom)
                validResponse = True
            elif toMoveFrom in indices:
                fromIdx = int(toMoveFrom) - 1
                validResponse = True
            else:
                print("")
                print("Invalid choice - please try again.")
                displayList(currentList)

        validResponseTwo = False
        while not validResponseTwo:
            indices = [str(x) for x in range(1, len(currentList) + 1)]
            print("")
            print(f"(Currently moving {fromIdx+1}. {currentList[fromIdx]})")
            print("Enter an item or position to move to:")
            toMoveTo = input(" --> ")           

            if toMoveTo in currentList and toMoveTo != currentList[fromIdx]:
                toIdx = currentList.index(toMoveTo)
                validResponseTwo = True
            elif toMoveTo in indices and toMoveTo != str(fromIdx + 1):
                toIdx = int(toMoveTo) - 1
                validResponseTwo = True
            else:
                print("")
                print("Invalid choice - please try again.")
                displayList(currentList)            

        currentList.insert(toIdx, currentList.pop(fromIdx))
        displayList(currentList)

        validResp = False
        while not validResp:
            print("")
            print("Move another item? (y/n)")
            resp = input(" --> ").lower()

            if resp in ["y", "yes"]:
                validResp = True
            elif resp in ["n", "no"]:
                validResp = True
                movingItems = False
            else:
                print("")
                print("Invalid response - please try again.")

        saveList(currentList)


def displayOptions():
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print("                LIST MANAGER - OPTIONS")
    print("")
    print("                1. View List")
    print("                2. Add Item(s)")
    print("                3. Remove Item(s)")
    print("                4. Edit Item(s)")
    print("                5. Move Item(s)")
    print("                6. Exit")
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION DEFINITION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    appOn = True

    while appOn:
        groceries = loadList()

        displayOptions()
        print("Choose a menu option:")
        userChoice = input(" --> ").lower()

        if userChoice in ["1", "1.", "1. view list", "1 view list", "view list"]:
            displayList(groceries)
        elif userChoice in ["2", "2.", "2. add items", "2 add items", "add items"]:
            addItems(groceries)
        elif userChoice in ["3", "3.", "3. remove items", "3 remove items", "remove items"]:
            removeItems(groceries)
        elif userChoice in ["4", "4.", "4. edit items", "4 edit items", "edit items"]:
            editItems(groceries)
        elif userChoice in ["5", "5.", "5. move items", "5 move items", "move items"]:
            moveItems(groceries)
        elif userChoice in ["6", "6.", "6. exit", "6 exit", "exit"]:
            appOn = False
        else:
            print("")
            print("Invalid option - try again!")



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION CALL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
main()
