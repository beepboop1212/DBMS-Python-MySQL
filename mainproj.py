
#Project on Ice Cream Showroom Management System
#---------------------------------------------------------------------------------------------------


#MODULE:Showroom MANAGMENT
import menushow
import icecream
import sales



def main():
 while True:
    icecream.clrscreen()
    print("\t\t\t ICE CREAM PARLOUR SALES MANAGEMENT \n")
    print("==============================================================================")
    print("1.PRODUCT RECORD MANAGEMENT")
    print("2.CUSTOMER RECORD MANAGEMENT")
    print("3.PRODUCT SALES RECORD MANAGEMENT")
    print("4.Exit")
    print("==============================================================================")
    choice = int(input("Enter Choice between 1 to 4 -----------> :"))
    if choice == 1:
                 menushow.menuicecream()
    elif choice==2:
                 menushow.menucustomer()
    elif choice==3:
                 menushow.menusales()
    elif choice==4:
                 break
    else:
            print("Wrong choice . . . . . . . Enter your choice again")
            x=input("Enter any key to continue")

    


if  __name__ == '__main__':
      main()
