##Starting function

def desc1():

    "This function has the details about the game for the user interface."
    print ("-------------------------------------------------------------------------------")
    print ("\n",'{:^70}'.format ("MASTERMIND\n\n"))
    print ("Number to Guess - XXXX",'{0:>33}'.format ("Colour Mapping:\n"))
    print ('{0:>70}'.format ("1-White  2-Blue  3-Red\n"),'{0:>74}' .format ("4-Yellow  5-Green  6-Purple\n"))
    print ("Enter 0000 as your guess if you wish to exit the game...\n")

    return


