#this is my base software
# TODO: Add comment blocks to all functions
# TODO: Add comment blocks to all programs and micro services
# TODO: Create main functionality broken into smaller functions
# TODO: Figure out how to save password (can make a txt file, make sure permissions make sense)
# TODO: Figure out how to save the entries
# TODO: ASCII Text title of program
# TODO: (Future implementation add Cryptography to encrypt entries before saving them and decrypt before reading, maybe sprint 2! Great micro service too. Maybe input is a txt file and same with output idk, or path name whichever works best across languages. OSs will be a problem.)
# TODO: (Future microservice ideas: Encrypt text, decrypt text, edit and update text file, random number generator, ascii art printer, positive affirmation generator, )


# Globals, all option statuses are booleans, more to be added in future iterations
passwordExists = False  # true if the password has been set previously
firstTimeSetUp = False  # true if the

# referenced globals
menubool = True
wrongpass = True
enabled = False
password = ""
exitbool = True

# TODO fix this function first
def entries():
    global menubool
    while menubool:
        print("Please enter the corresponding number from the following menu options:\n")
        print("[1] View entries\n")
        print("[2] Create new entry\n")
        print("[3] Delete an entry\n")
        print("[4] Go Back\n")
        user_input = input()
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            menubool = False
        else:
            print("Error: Menu option not found. Please enter the chosen number.\n")


def passwordfunc():
    global wrongpass, password
    while wrongpass:
        print("Please enter your password: ")
        user_input = input()
        if user_input == password:
            print("Please enter your password: ")
            wrongpass = False
        else:
            print("Error: Incorrect Password")


def options():
    global menubool, passwordExists, enabled, password
    while menubool:
        print("Welcome to Options. Options have their status written next to them. More complex options may prompt you for more information.\n")
        print("These changes can be reversed. Please enter the corresponding number from the following menu options:\n")
        print("[1] Password [enabled variable]\n", enabled)
        print("[2] Go Back\n")
        user_input = input()
        if user_input == "1":
            if passwordExists:
                print("Please enter your new password. If you would like to disable the password, do not:\n")
            else:
                pass
        elif user_input == "2":
            menubool = False
        else:
            print("Error: Menu option not found. Please enter the chosen number.\n")


def main():
    global exitbool, passwordExists
    while exitbool:
        print("Welcome to your digital journal!\n")
        if passwordExists:
            passwordfunc()
        print("Please enter the corresponding number from the following menu options:\n")
        print("[1] Manage entries\n")
        print("[2] Options\n")
        print("[3] Quit\n")
        user_input = input()

        if user_input == "1":
            entries()
        elif user_input == "2":
            options()
        elif user_input == "3":
            exitbool = False  # fixed: assignment, not comparison
        else:
            print("Error: Menu option not found. Please enter the chosen number.\n")


# call main (keeps behavior similar to your pseudocode)
main()
