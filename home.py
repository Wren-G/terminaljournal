#this is my base software
# TODO: Add comment blocks to all functions
# TODO: Add comment blocks to all programs and micro services
# TODO: Figure out how to save password (can make a txt file, make sure permissions make sense)
# TODO: (Future implementation add Cryptography to encrypt entries before saving them and decrypt before reading, maybe sprint 2! Great micro service too. Maybe input is a txt file and same with output idk, or path name whichever works best across languages. OSs will be a problem.)
# TODO: (Future microservice ideas: Encrypt text, decrypt text, edit and update text file, random number generator, ascii art printer, positive affirmation generator, )
# TODO: Replace all passes with code
# TODO: decide how array can be stored and parsed please

import os #operating system commands

# Globals, all option statuses are booleans, more to be added in future iterations
#TODO: settings array variable 
firstTimeSetUp = True  # false if the user has logged in before (checking settings.txt file)
passwordExists = False  # true if the password has been set previously


# referenced globals
menubool = True
wrongpass = True
enabled = False
password = ""
exitbool = True

#This function reads the text file 'settings.txt' and 'password.txt' which contains settings for the user's data
#settings array
def readData():
    #settings.txt will be a string of 1s and 0s, in order of array spot
    #the array is a character array with ten spots acting as 0 or 1 booleans
    #the array will be further widened as the program gets further in development
    #spot 0 is firstTimeSetUp
    #spot 1 is passwordExists
    #password.txt just contains the users journal password
    #if password exists:
    #reads password.txt and sets password variable to it
    #if password does not exist:
    #do not read or look for password.txt
    print("hi")

#This function runs through extra information if the user has not opened Pocket Journal before
def firstStart():
    #informs the user that this tool will modify their files. Asks if they would like to proceed
    #if the user proceeds, continue, otherwise exit program
    #creates the folder for Pocket Journal
    #creates settings.txt TODO: Should I just add the file in github? That way I 
    # can have the default settings in there already on first download
    #starts by saving information to settings.txt in set format
    #first time starting pocket journal, in which case, default settings are set
    #for first time setup, user should be told where entries will be stored
    #should tell the user for first time setup that it will be modifying files on the users computer
    print("hi")

#This function allows users to select and delete entries, deleting the text files that hold them
def deleteentry():
    print("hi")


#This function allows users to create text files /  entries on their computer
#This function also creates the folder 'journal entries' if it does not exist
def createentry():
    folder = "journalentries"
    #ensure the folder exists and makes the folder if first start up
    os.makedirs(folder, exist_ok=True)
    print("Please enter the name of the new journal entry.")
    entryname = input().strip()
    if entryname == "":
        print("Error: Entry name cannot be empty.")
        return
    #ensure file is a txt file
    if not entryname.lower().endswith(".txt"):
        filename = entryname + ".txt"
    else:
        filename = entryname
    #save path of file
    abs_path = os.path.abspath(os.path.join(folder, filename))
    print(f"{filename} successfully created. You may now type your entry. Hitting 'enter' will save")
    print("and close your submission.\n")
    entry_text = input()

    # write entry_text into txt file
    with open(abs_path, "w", encoding="utf-8") as f:
        f.write(entry_text)
    print(f"Entry {filename} saved in path: {abs_path}")




#This function will allow users to look at their entries
def showentries():
    print("hi")


# This function is just a sub menu for entry related option in pocket journal.
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
            showentries()
        elif user_input == "2":
            createentry()
        elif user_input == "3":
            deleteentry()
        elif user_input == "4":
            menubool = False
        else:
            print("Error: Menu option not found. Please enter the chosen number.\n")

#Password function has the user enter their password, if the password is 
#incorrect 3 times, the program exits
def passwordfunc():
    global wrongpass, password
    counter = 0
    while wrongpass:
        print("Please enter your password: ")
        user_input = input()
        if user_input == password:
            print("Welcome back!")
            wrongpass = False
        else:
            print("Error: Incorrect Password")
            counter = counter + 1
            if counter == 3:
                print("Too many incorrect password attempts. Goodbye.")
                #TODO: exit


def options():
    global menubool, passwordExists, enabled, password
                                 
    print(" _____     _   _             ")
    print("|     |___| |_|_|___ ___ ___ ")
    print("|  |  | . |  _| | . |   |_ -|")
    print("|_____|  _|_| |_|___|_|_|___|")
    print("      |_|                    \n")
    while menubool:
        print("Welcome to Options. Options have their status written next to them.")
        print("More complex options may prompt you for more information.\n")
        print("These changes can be reversed. Please enter the corresponding number from the following menu options:\n")
        print("[1] Password [enabled variable]\n", enabled) #TODO fix this line for the variable
        print("[2] Save and Go Back\n")
        user_input = input()
        if user_input == "1":
            if passwordExists:
                print("Please enter your new password. If you would like to disable the password,")
                print("do not type anything, and hit 'enter'.\n")
                user_input = input()
                if user_input == "":
                    passwordExists = False
                else:
                    password = user_input
                    passwordExists = True 
            else:
                pass
        elif user_input == "2":
            #TODO: save user data before exiting options
            menubool = False
        else:
            print("Error: Menu option not found. Please enter the chosen number.\n")

#this function brings up the wall of text that is the Help page
#It just works as documentation for the app
def helpdoc():
                     
    print(" _____     _     ")
    print("|  |  |___| |___ ")
    print("|     | -_| | . |")
    print("|__|__|___|_|  _|")
    print("            |_|  \n")
    print("Welcome to the Help page! Here you will find information on how to use this application,")
    print("As well as some Frequently Asked Questions. (FAQ)\n")
    print("Hit Enter to close the Help page.\n")
    print("----Information on Entries----")
    print("Entries is this application's term for the text files the user can submit on this application.")
    print("Using this application, users can type out whatever they'd like, and the application will")
    print("automatically save these text files to the user's local storage on their current computer.")
    print("It will be located wherever the user installed Pocket Journal.\n")
    print("Entries can be viewed or deleted, but cannot currently be edited.\n")
    print("Entries will automatically be given a date based on the user computer's current date at the")
    print("time of submission.\n")
    print("To create, view, or delete an entry, navigate through the menu by entering the number next to")
    print("the menu option (like you did to get to this page) 'Entries', in this case, option number 1.\n")
    print("---WARNING---")
    print("When deleting an entry, it is unable to be recovered or undone!\n")
    print("----Information on Options----")
    print("Options allow you to customize the application in ways unique to your copy of this application.")
    print("Each option can be toggled on and off by entering the number next to the option of your choice.")
    print("Some options will be ticked on or off by default. Some options will have extra prompts or")
    print("sub-menus if they need extra input to be enabled or disabled. You should read carefully to")
    print("ensure you understand each option before enabling or disabling them. Options corresponds to number")
    print("2 in the main menu. Navigate through the menu by entering the number next to the menu option that")
    print("you would like to open.\n")
    print("-Password-")
    print("This option will allow you to add, remove, or change your password. Passwords are great for")
    print("keeping your journal private, however they will need to be remembered or they may lock you out too!\n")
    print("----FAQ----")
    print("Q: Where are my journal entries stored?")
    print("A: They are automatically stored in the same location Pocket Journal is downloaded / executed.")
    print("They are in a sub folder named 'journalentries'.") #TODO: Make sure this is right
    print("\n")
    print("")

    print("Hit enter to close Help and go back.")
    user_input = input()

#Startup sequence
#then, main will check for settings.txt and import all the saved settings, if it is not found, it is the users
#first time starting pocket journal, in which case, default settings are set
#for first time setup, user should be told where entries will be stored
#should tell the user for first time setup that it will be modifying files on the users computer
def main():
    global exitbool, passwordExists
    print("   ___           __       __       __                        __  ")
    print("  / _ \___  ____/ /_____ / /_  __ / /__  __ _________  ___ _/ /  ")
    print(" / ___/ _ \/ __/  '_/ -_) __/ / // / _ \/ // / __/ _ \/ _ `/ /   ")
    print("/_/   \___/\__/_/\_\\__/\__/   \___/\___/\_,_/_/ /_//_/\_,_/_/   ")
    print("\n")
                                                                 
    print("Welcome to Pocket Journal, your local, digital journal managing application. Make entries to read later!\n")
    print("\n")
    readData()
    if firstTimeSetUp: #If the user has not used Pocket Journal before
        firstStart()
    if passwordExists:
        passwordfunc()
    while exitbool:
        print("Please enter the corresponding number from the following menu options:\n")
        print("[1] Manage entries\n")
        print("[2] Options\n")
        print("[3] Help\n")
        print("[4] Save and Quit\n")
        user_input = input()

        if user_input == "1":
            entries()
        elif user_input == "2":
            options()
        elif user_input == "3":
            helpdoc()
        elif user_input == "4":
            exitbool = False  
        else:
            print("Error: Menu option not found. Please enter the chosen number.\n")

# Program calls main function, 
main()
