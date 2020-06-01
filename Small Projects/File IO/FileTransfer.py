import shutil
import os
import time

class DayChecker:
    # Creates variables and prints welcome message
    def __init__(self): 
        self.source = "None"
        self.destination = "None"
        self.files = []
        self.repeat = True
        print("Welcome to the 24 hour file checker!")
        print("Type 'inst' for instructions")

    # Prints File Directories  
    def PrintInfo(self): 
        print("Source: {}\nDestination: {}".format(self.source, self.destination))

    # Checks to see if there are files at the directory and asks user if they want to proceed
    def CheckFiles(self): 
        self.files = os.listdir(self.source) # Sets files to the files in the source directory
        # Checks if there are 0 files in the directory
        # Returns if there are none
        if len(self.files) == 0:
            print("\n===================================")
            print("There are no files in this location")
            print("===================================\n")
            return
        # Lists files in directory and asks if the user wants to continue
        else:
            print("\n===================================")
            print("Files at {}:".format(self.source))
            for f in self.files:
                print("\t{}".format(f))
            print("\nWould you like to continue? (y/n)")
            print("===================================\n")
            inpt = input("> ")
            # Tests just the first letter to account for 'y' or 'yes' upper and lower
            if inpt.lower()[0] == 'y':
                self.MoveFilesIfTFH()
            else:
                print("\n===================================")
                print("Operation canceled. \nYou may enter more commands.")
                print("===================================\n")
                return
                
    # Moves the files if they were edited in the past 24 hours    
    def MoveFilesIfTFH(self):
        movedFiles = [] # Resets the movedFiles list
        for f in self.files:
            testFile = self.source + f # Created the file path
            testEditTime = os.path.getmtime(testFile) + 86400 # Gets the edit time and adds 24 hours to it 
            # Tests the edit time compared to current time to see if edited in 24 hours
            # Moves the files and adds them to the list
            # Tries to catch an error if the directory doesnt exist. Prints out the file that gave the error
            if testEditTime > time.time():
                try:
                    shutil.move(testFile, self.destination)
                except:
                    print("\n===================================")
                    print("[ERROR] An Error occured while trying to move files. \nMake sure you have the correct directories")
                    print("Error occured on file: {}".format(testFile))
                    print(sys.exc_info()[0])
                    print("===================================\n")
                    return
                movedFiles.append(f)
        print("\n===================================")
        print("{} files moved".format(len(movedFiles))) # Prints number of files moved
        print("Files moved:")
        # Prints the moved files
        for i in range(len(movedFiles)):
            print("\t{}".format(movedFiles[i]))
        print("New directory: {}".format(self.destination)) # Prints new directory files were moved to
        print("===================================\n")
            
                    
        
    # Gets user's inpput and executes commands
    def CheckUserInput(self, inpt):
        inpt = inpt.lower()

        # Breaks the main loop thus ending the program
        if inpt == "close":
            self.repeat = False

        # Prints Instructions
        elif inpt == "inst":
            print("\n===================================")
            print("Type in the text in the '' to execute a command.\nCommands:")
            print(": 'src \{path\}'\n\tSets the source directory")
            print(": 'dest \{path\}'\n\tSets the destination directory")
            print(": 'run'\n\tWill take the files from the source and put them into the destination directory if they have been edited in the past 24 hours")
            print(": 'close'\n\tCloses the program")
            print(": 'inst'\n\tPrints out the possible commands")
            print("===================================\n")

        # Runs the primary function
        elif inpt == "run":
            self.CheckFiles()

        else:
            spcIndex = -1 # Sets to -1 to test if there is no space
            # Test if each input character is a space and saves it's index
            for c in range(len(inpt)):
                if inpt[c] == " ":
                    spcIndex = c
                    break # If there was a space in the file directory, it would come up as an invalid command
            cmd = inpt[0 : spcIndex] # Sets the first word to cmd
            path = inpt[(spcIndex+1) : len(inpt)] # Sets second word to the directory path
            # Adds a slash to the end in case the user didn't
            if path[len(path)-1] is not '\\' or path[len(path)-1] is not '/':
                path += '\\'
            # If the command was 'src' sets the input to the source directory
            if cmd == "src":
                self.source = path
                print("\n===================================")
                self.PrintInfo()
                print("===================================\n")
            # If the command was 'dest' sets the input to the destination directory
            elif cmd == "dest":
                self.destination = path
                print("\n===================================")
                self.PrintInfo()
                print("===================================\n")
            # Tests if user entered wrong command
            else:
                print("\n===================================")
                print("[ERROR] Invalid Command! Type 'inst' for a list of commands")
                print("===================================\n")
            



if __name__ == "__main__":
    print("\n===================================")
    # Creates the class and prints welcome with default values
    dc = DayChecker()
    dc.PrintInfo()
    print("===================================\n")
    # Main gameplay loop
    while(dc.repeat):
        # Allows user to input a command
        dc.CheckUserInput(input("> "))
        
        
        
        
