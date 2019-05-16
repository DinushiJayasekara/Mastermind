
##Calling single functions with different names
import Game_Details.desc_user_interface as details
import Game_Details.desc_txtfile as details_txt

##Calling entire 'Code' module
import Code

##Starting function
def main_menu():
    "This function contains the main menu of the game"
    print ("1. PLAY THE GAME\n2. EXIT THE GAME\n")

    ##Displaying error if user enters values that aren't integers
    try:
        menu=int(input("Choose 1 or 2 from above menu:"))
    except ValueError:
        print("\nPLEASE ENTER 1 OR 2 AS YOUR CHOICE!\n")
        print("-------------------------------------\n")
        ##Calling 'main_menu' inside 'Menu' module
        main_menu()
   
    ##Exiting game if user enters 2
    if menu==2:
        exit()
    else:
        ##Starting game if user enters 1
        if menu==1:
            ##Calling 'desc_user_interface' inside 'Game_Details' module
            details.desc1()
            ##Calling 'desc_txtfile' inside 'Game_Details' module
            details_txt.desc2()
            ##Calling 'main_code' inside 'Code' module
            Code.main_code()
        else:
            ##If user enters number other than 1 or 2
            if menu!=1 or menu!=2:
                print("\nPLEASE ENTER 1 OR 2 AS YOUR CHOICE!\n")
                print("-------------------------------------\n")
                ##Calling 'main_menu' inside 'Menu' module
                main_menu()
    return
