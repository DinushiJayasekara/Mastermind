##Calling single functions with different names
import Game_Details.desc_user_interface as details
import Game_Details.desc_txtfile as details_txt

##Starting function
def main_code():
    "This function contains the main code for the program"

    ##System generates 4 random digits within the range 1-6...
    import random
    value1=random.randrange(1,7)
    value2=random.randrange(1,7)
    value3=random.randrange(1,7)
    value4=random.randrange(1,7)
    code=[value1,value2,value3,value4]
    
    ##Converting list into string...        
    hidden_code=" ".join(map(str,code))
    
    ##User can have a maximum of 8 guesses
    count=1
    while (count<=8):

        ##Creating text file to store game data
        textfile=open("ResultFile.txt","a")

        ##Allowing user to enter the 4 digits of 1 guess seperately...
        ##Displaying error if user enters values that aren't integers        
        try:
            guess1=int(input("Enter the first digit of your guess:"))
            guess2=int(input("Enter the second digit of your guess:"))
            guess3=int(input("Enter the third digit of your guess:"))
            guess4=int(input("Enter the fourth digit of your guess:"))
        except ValueError:
            print ("\nPLEASE ENTER INTEGERS FOR ALL DIGITS!\nRESTARTING GAME...")
            ##Writing in text file
            print("\nERROR IN USER'S INPUT FOR INTEGER VALUES\nRESTARTING GAME...",file=open("ResultFile.txt","a"))
            textfile.write("----------------------------------------------------------\n")
            ##Calling 'desc_user_interface' inside 'Game_Details' module
            details.desc1()
            ##Calling 'desc_txtfile' inside 'Game_Details' module
            details_txt.desc2()
            ##Calling 'main_code' inside 'Code' module
            main_code()
   
        ##Converting list into string
        guess=[guess1,guess2,guess3,guess4]
        final_guess=" ".join(map(str,guess))
        
        ##Checking if guessed digits match the random number digits 
        correct=0
        half=0
        wrong=0

        for i in range(0,4):

            if (guess[i]==code[i]):
                correct=correct+1
            elif (guess[i] in code):
                half=half+1
            else:
                wrong=wrong+1
                continue

        output=""
        for i in range(correct):
            output=output+"1"
        for i in range(half):
            output=output+"0"
        for i in range(wrong):
            output=output+"."

        ##Convert string into list        
        result=list(output)
        ##Shuffling the elements of the list
        random.shuffle(result)
        ##Converting list back into string
        final_result=''.join(result)
                    
        ##Displaying message if user wins game
        if (final_result=="1111"):
            print ("\nTry No: ",count, '{:>25}'.format("Guess: "),final_guess, '{:>25}'.format ("Result: 1111"))
            print("\nCONGRATULATIONS!!!!! YOU HAVE WON THE GAME...")
            newgame=input("\nDo you want to play another game (Yes/No)?")
            
            ##Asking if user wants to play new game after winning...
            ##Writing results of game in text file                    
            if newgame=="Yes" or newgame=="yes" or newgame=="YES":
                print("\nCONGRATULATIONS!!!!! YOU HAVE WON THE GAME...",file=open("ResultFile.txt","a"))
                print("\nYOUR GUESS",final_guess," WAS CORRECT!",file=open("ResultFile.txt","a"))
                print("\nSTARTING NEW GAME AS PER USER'S REQUEST...",file=open("ResultFile.txt","a"))
                ##Calling 'desc_user_interface' inside 'Game_Details' module
                details.desc1()
                ##Calling 'desc_txtfile' inside 'Game_Details' module
                details_txt.desc2()
                ##Calling 'main_code' inside 'Code' module
                main_code()
            else:                                    
                ##If user wants to exit game after winning...
                ##Writing results of game in text file                    
                print("\nCONGRATULATIONS!!!!! YOU HAVE WON THE GAME...",file=open("ResultFile.txt","a"))
                print("\nYOUR GUESS",final_guess," WAS CORRECT!",file=open("ResultFile.txt","a"))
                print("\nQUITTING GAME AS PER USER'S REQUEST...",file=open("ResultFile.txt","a"))
                textfile.write("----------------------------------------------------------\n")
                exit()

        ##If user quits game by entering 0000 as guess...
        if (guess1==0 and guess2==0 and guess3==0 and guess4==0):
            ##Writing data into text file
            print("\nUSER ENTERED 0000 AS GUESS...",file=open("ResultFile.txt","a"))
            print("\nQUITTING GAME AS PER USER'S REQUEST.",file=open("ResultFile.txt","a"))
            textfile.write("----------------------------------------------------------\n")
            input ("\nGAME ENDED...")
            ##Exiting game as user entered 0000 as guess                
            exit()                
        else:
            ##Displaying error message if user's guess has numbers outside 1-6              
            if (guess1<1 or guess1>6 or guess2<1 or guess2>6 or guess3<1 or guess3>6 or guess4<1 or guess4>6):
                print ("\nTry No:",count, '{:>32}'.format("Guess: NOT VALID"), '{:>30}'.format ("Result: NO RESULT"))
                print ("\nPLEASE ENTER VALUES BETWEEN 1 AND 6 FOR ALL DIGITS...\n")               
                ##Storing data in text file
                textfile.write("\nTry No: %s\n" % count)
                textfile.write("Guess: NOT VALID\n")
                textfile.write("Result: NO RESULT\n")
                textfile.write("\nPLEASE ENTER VALUES BETWEEN 1 AND 6 FOR ALL DIGITS...\n")
            else:
                ##If no errors in user's input                    
                print ("\nTry No: ",count, '{:>25}'.format("Guess: "),final_guess, '{:>25}'.format ("Result: "),final_result)
                print ()
                ##Writing data into text file
                textfile.write("\nTry No: %s\n" % count)
                textfile.write("Guess: %s\n" % final_guess)
                textfile.write("Result: %s\n" % final_result)

        ##Increasing value of count after 1 try is over
        count=count+1

    ##While loop ends here...
        
    ##Writing data into text file            
    textfile.write("\nOOPS... YOU HAVE RUN OUT OF TRIES!\n\nThe correct code is %s\n" % hidden_code)
    textfile.write("----------------------------------------------------------\n")
    ##Displaying error message after player uses 8 tries            
    print ("---------------------------------------------------------------------------------")
    print ("\nOOPS... YOU HAVE RUN OUT OF TRIES!\n\nThe correct code is ",hidden_code)
    ##If user wants to play new game after running out of tries...
    newgame2=input("\nDo you want to play another game (Yes/No)?")            
    if newgame2=="Yes" or newgame2=="yes" or newgame2=="YES":
        ##Storing results of game in text file
        print("\nSTARTING NEW GAME AS PER USER'S REQUEST...",file=open("ResultFile.txt","a"))
        textfile.write("----------------------------------------------------------\n")
        ##Calling 'desc_user_interface' inside 'Game_Details' module
        details.desc1()
        ##Calling 'desc_txtfile' inside 'Game_Details' module
        details_txt.desc2()
        ##Calling 'main_code' inside 'Code' module
        main_code()
    else: 
        ##If user wants to exit game after running out of tries...
        exit()

    ##Closes text file        
    textfile.close()
    return
