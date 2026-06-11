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


def saveList():
    pass


def displayList():
    pass


def addItems():
    pass


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
            displayList()
        elif userChoice in ["2", "2.", "2. add items", "2 add items", "add items"]:
            addItems()
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
