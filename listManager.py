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
        newSave.writelines(listIn)


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

    while addingItems:
        displayList(currentList)
        print("")
        print("Enter an item to add:")
        toAdd = input(" --> ")
        currentList.append(toAdd)

        validResp = False
        if not validResp:
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


def removeItems():
    pass


def editItems():
    pass


def moveItems():
    pass


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
            removeItems()
        elif userChoice in ["4", "4.", "4. edit items", "4 edit items", "edit items"]:
            editItems()
        elif userChoice in ["5", "5.", "5. move items", "5 move items", "move items"]:
            moveItems()
        elif userChoice in ["6", "6.", "6. exit", "6 exit", "exit"]:
            appOn = False
        else:
            print("")
            print("Invalid option - try again!")



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN FUNCTION CALL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
main()
