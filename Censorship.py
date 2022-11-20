# Programmed by: Lee Anne Y. Angeles

file = open("INPUT.txt", "w")                                                         # Open text file in write mode
poem = """Where do people go to when they die?
Somewhere down below or in the sky?
'I can't be sure,' said Grandad, 'but it seems
They simply set up home inside our dreams."""                                         # A variable that contains a poem
file.write(poem)                                                                      # Write the output in text file
file.close()                                                                          # Close the file

while True:                                                                           # While statement for looping
    try:
        poemFile = open("INPUT.txt", "r")                                             # Open text file in read mode
    except FileNotFoundError:                                                         # Exception if file does not exist
        print("File Does Not Exist")                                                  # Display 'File does not exist'
    else:                                                                             # Else statement
        readPoem = poemFile.read()                                                    # Read the contents of text file
        replace = input("\nEnter character to replace: ")                             # Inputs statement
        if replace in readPoem:                                                       # If statement
            insert = input("Enter character to insert: ")                             # Input statement
            newFile = open("REPLACE.txt", "w")                                        # Open a new file in write mode
            encryptedPoem = readPoem.replace(replace, insert)                         # Replace char to new char
            newFile.write(str(encryptedPoem))                                         # Write output to new text file
            newFile.close()                                                           # Close the file
            break
        else:                                                                         # Else statement
            print("The character '{}' did not match any characters in the poem!".format(replace))
            print("Please try again!")                                                # Display try again
            continue                                                                  # Continue for looping
