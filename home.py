#Wren Gilbert
#Pocket Journal, a terminal journaling app
#This program is my main implementation, all functions here have comments to explain them
# TODO: Add comment blocks to all functions
# TODO: Add comment blocks to all programs and micro services
# TODO: (Future implementation add Cryptography to encrypt entries before saving them and decrypt before reading, maybe sprint 2! Great micro service too. Maybe input is a txt file and same with output idk, or path name whichever works best across languages. OSs will be a problem.)
# TODO: (Future microservice ideas: Encrypt text, decrypt text, edit and update text file, random number generator, ascii art printer, positive affirmation generator, )
# TODO: (future implementation add flags for encryption and things like the ascii and words of affirmation for more user experience)
# TODO: For all microservice and settings adjustments, first time start up, readdata, help, options, and even settings.txt all need updates

import os #operating system commands
import sys #for system exit

# Globals, all option statuses are booleans, more to be added in future iterations
settings = ['0'] * 10  # character array of ten spots, 0 or 1
firstTimeSetUp = True  # false if the user has logged in before (checking settings.txt file)
passwordExists = False  # true if the password has been set previously


# referenced globals
menubool = True # used for while loops
wrongpass = True # used for password function
password = "" # holds password string
exitbool = True # main menu while loop

#save function should write the settings array into the text file
#save function also calls readdata to ensure that the program is always up to date and a call is not missed
def saveSettings():
    global settings
    bits = [c if c in "01" else "0" for c in settings]
    if len(bits) < 10:
        bits += ["0"] * (10 - len(bits))
    else:
        bits = bits[:10]
    out = "".join(bits)

    with open("settings.txt", "w", encoding="utf-8") as f:
        f.write(out)

    readData()


#This function reads the text file 'settings.txt' and 'password.txt' which contains settings for the user's data
#settings array should be updated with this information
def readData():
    global settings, firstTimeSetUp, passwordExists, password
    with open("settings.txt", "r", encoding="utf-8") as f:
        raw = f.read()
    bits = [c for c in raw if c in "01"]
    #ensure we have exactly 10 (for now) (for other coders, this is for my future settings slots / global flags)
    if len(bits) < 10:
        bits += ["0"] * (10 - len(bits))
    else:
        bits = bits[:10]
    settings = bits 

    #parse settings array to apply setting preset
    firstTimeSetUp = True if settings[0] == "1" else False
    passwordExists = True if settings[1] == "1" else False

    #only read password.txt if a password exists
    password = ""
    if passwordExists:
        with open("password.txt", "r", encoding="utf-8") as pf:
            password = pf.read().rstrip("\n")
    #return the array just in case
    return settings


#This function runs through extra information if the user has not opened Pocket Journal before
def firstStart():
    global settings, firstTimeSetUp, passwordExists
    #informs the user that this tool will modify their files. Asks if they would like to proceed
    print("It seems this is your first time opening Pocket Journal.")
    print("There are a few things to be aware of for your first time, such as how")
    print("this program functions. This executable will be capable of altering and")
    print("creating files locally on your computer. If this is objectionable")
    print("to you in any way, please exit the program.\n")
    print("If you are not opposed to this. Hit 'Enter'.\n")
    user_input = input()
    print("Entries will be stored in the same directory as this executable.")
    print("To begin Journal initialization, please hit 'Enter'.")
    user_input = input()
    #creates the folder 'journalentries' if it does not exist
    folder = "journalentries"
    os.makedirs(folder, exist_ok=True)
    # starts by saving information to settings.txt in set format
    # write 00 to the text file (no password, no first time setup prompt)
    settings[0] = "0"
    settings[1] = "0"
    saveSettings() #save settings
    #first time starting pocket journal, in which case, default settings are set
    print("journalentries folder has been created.")
    print("Settings have been updated.")
    print("Thank you for using Pocket Journal!")


#This function allows users to user_inputect and delete entries, deleting the text files that hold them
def deleteEntry():
    global menubool
    folder = "journalentries"

    files = [f for f in os.listdir(folder) if f.endswith(".txt")]
    if not files:
        print("No journal entries found to delete.\n")
        return
    menubool = True
    while menubool:
        # list all journal entries
        for i, name in enumerate(files, start = 1):
            print(f"[{i}] {name}")
        print("[0] Back")
        print("Above are your previously made journal entries, listed as their file name in your computer.")
        print("They are organized by last edited. To delete one, enter the number corresponding to the desired file.")
        try:
            user_input = int(input())
        except ValueError:
            print("Error: Please enter a valid number.\n")
            return

        # validate user_inputection
        if user_input < 0 or user_input >= len(files):
            print("Error: Entry number not found.\n")
            return
        elif user_input == 0:
            break

        filename = files[user_input]
        filepath = os.path.join(folder, filename)

        # confirmation loop
        while menubool:
            print("Are you sure you want to delete the current entry? This choice is irreversible, and the file")
            print("will be unable to be recovered. (Y/N)")
            confirm = input().strip().upper()
            if confirm == "Y":
                try:
                    os.remove(filepath)
                    print(f"Journal entry '{filename}' has been deleted.")
                except OSError as e:
                    print(f"Error: Unable to delete file '{filename}': {e}")
                break
            elif confirm == "N":
                break
            else:
                print("Error: Menu option not found. Please enter the chosen letter.\n")


    


#This function allows users to create text files /  entries on their computer
#This function also creates the folder 'journal entries' if it does not exist
def createEntry():
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



#TODO make this more modular
#This function will allow users to look at their entries
#There is also an option for the users to delete their entries if they so wish
def showEntries():
    global menubool, settings
    folder = "journalentries"

    # ensure folder exists and contains .txt files
    if not os.path.exists(folder):
        print("No journalentries folder found. There are no entries to view.\n")
        return

    files = [f for f in os.listdir(folder) if f.endswith(".txt")]
    if not files:
        print("No journal entries found to view.\n")
        return

    # sort by last edited time, newest first
    files.sort(key=lambda f: os.path.getmtime(os.path.join(folder, f)), reverse=True)

    menubool = True
    while menubool:
        #list all journal entries
        for i, name in enumerate(files, start=1):
            print(f"[{i}] {name}")
        print("[0] Back")
        print("Above are your previously made journal entries, listed as their file name in your computer.")
        print("They are organized by last edited. To view one, enter the number corresponding to the desired file.")

        user_input = input().strip()
        try:
            user_input_num = int(user_input)
        except ValueError:
            print("Error: Please enter a valid number.\n")
            continue

        if user_input_num == 0:
            return

        if user_input_num < 1 or user_input_num > len(files):
            print("Error: Entry number not found.\n")
            continue

        index = user_input_num - 1
        filename = files[index]
        filepath = os.path.join(folder, filename)

        # print file contents
        try:
            with open(filepath, "r", encoding="utf-8") as rf:
                content = rf.read()
        except OSError as e:
            print(f"Error: Unable to open file '{filename}': {e}\n")
            try:
                files.pop(index)
            except Exception:
                pass
            if not files:
                print("No remaining journal entries.\n")
                return
            continue

        print(f"\n--- {filename} ---\n")
        if content:
            print(content)
        else:
            print("(This entry is empty.)")
        print("\n--- End of entry ---\n")

        while True:
            print("Please enter the corresponding number from the following menu options:\n")
            print("[1] Delete Current Entry\n")
            print("[2] Back\n")
            user_input = input().strip()

            if user_input == "1":
                # confirmation loop
                while True:
                    print("Are you sure you want to delete the current entry? This choice is irreversible, and the file")
                    print("will be unable to be recovered. (Y/N)")
                    confirm = input().strip().upper()
                    if confirm == "Y":
                        try:
                            os.remove(filepath)
                            print(f"Journal entry '{filename}' has been deleted.")
                            files.pop(index)
                        except OSError as e:
                            print(f"Error: Unable to delete file '{filename}': {e}")
                        break  # exit confirmation loop
                    elif confirm == "N":
                        break  
                    else:
                        print("Error: Menu option not found. Please enter the chosen letter.\n")
                break
            elif user_input == "2":
                break
            else:
                print("Error: Menu option not found. Please enter the chosen number.\n")
        if not files:
            print("No remaining journal entries.\n")
            return



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
            showEntries()
        elif user_input == "2":
            createEntry()
        elif user_input == "3":
            deleteEntry()
        elif user_input == "4":
            break
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
                #TODO: ensure exit command is safe
                sys.exit()


#Options allows users to affect global variables, and saves them in a text file so they persist after 
#closing the application
def options():
    global menubool, passwordExists, password, settings
                                 
    print(" _____     _   _             ")
    print("|     |___| |_|_|___ ___ ___ ")
    print("|  |  | . |  _| | . |   |_ -|")
    print("|_____|  _|_| |_|___|_|_|___|")
    print("      |_|                    \n")
    while menubool:
        print("Welcome to Options. Options have their status written next to them.")
        print("More complex options may prompt you for more information.\n")
        print("These changes can be reversed. Please enter the corresponding number from the following menu options:\n")
        print(f"[1] Password {'enabled' if passwordExists else 'disabled'}\n") 
        print("[2] Save and Go Back\n")
        user_input = input()
        if user_input == "1":
            print("Please enter your new password. If you would like to disable the password,")
            print("do not type anything, and hit 'enter'.\n")
            user_input = input()
            with open("password.txt", "w", encoding="utf-8") as f:
                f.write(user_input)
            if user_input == "":
                settings[1] = "0" 
            else:
                password = user_input
                settings[1] = "1" #This does not change flags, just updates 
        elif user_input == "2":
            #save user data before exiting options
            saveSettings() #this changes the flags
            break
        else:
            print("Error: Menu option not found. Please enter the chosen number.\n")

#this function brings up the wall of text that is the Help page
#It just works as documentation for the app
#In the future, this may be a seperate document instead, or just the README file.
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
    print("They are in a sub folder named 'journalentries'.") 
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
    if passwordExists: #If the user has a password set up
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
