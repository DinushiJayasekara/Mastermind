##Starting function

def desc2():

    "This function stores the details about the game in text files."
    textfile=open("ResultFile.txt","a")
    textfile.write("----------------------------------------------------------\n")
    textfile.write("\t\t\tMASTERMIND\n\n")
    textfile.write("Number to Guess - XXXX\t\t\tColour Mapping:\n")
    textfile.write("\t\t\t\t\t1-White  2-Blue  3-Red\n\t\t\t\t\t4-Yellow  5-Green  6-Purple\n")

    return
