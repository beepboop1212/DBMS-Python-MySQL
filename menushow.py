#PYTHON MODULE : MENULIB


import icecream
import customer
import sales

def menuicecream():
    while True:
        icecream.clrscreen()
        print("\t\t\t Ice Cream Record Management\n")
        print("==============================================================================")
        print("1.Add Ice Cream Record")
        print("2.Display Ice Cream Record")
        print("3.Search Ice Cream Record")
        print("4.Delete Ice Cream Record")
        print("5.Update Ice Cream Record")
        print("6.Return To Main Menu")
        print("==============================================================================")
        choice=int(input("enter your choice between 1 to 5 ----------> :"))
        if choice ==1:
            icecream.insertdata()
        elif choice==2:
            icecream.display()
        elif choice==3:
            icecream.searchicecreamrec()
        elif choice==4:
            icecream.deleteicecream()
        elif choice==5:
            icecream.updateicecream()
            
        elif choice==6:
         #   updateicecream()
            return
        else:
            print("Wrong Choice. . . . . . . . . . Enter Your Choice Again")
            x= input("enter any key to continue")

#----------------------------------------------------------------------------------------------------------------
            
def menucustomer():
    while True :
        icecream.clrscreen()
        print("\t\t\t customer Record Management \n")
        print("==============================================================================")
        print("1.Add customer Record")
        print("2.Display customer Record")
        print("3.Search customer Records")
        print("4.Delete customer Records")
        print("5.Update customer Record")
        print("6.Return to Main Menu")
        print("==============================================================================")
        choice=int(input("Enter Choice  between 1 to 5 ----------> :"))
        if choice ==1:
            customer.insertcustomer()
        elif choice ==2 :
            customer.display()
        elif choice==3:
            customer.searchcustomer()
        elif choice==4:
            customer.deletecustomer()
        elif choice==5:
            customer.updatecustomer()
            print("no such function ")
        elif choice==6:
            return
        else:
            print("Wrong Choice. . . . . . . . . . . Enter Your Choice Again")
            x=input("Enter Any Key To  Continue")


#-----------------------------------------------------------------------------------------------------------------        


def menusales():
    while True:
        icecream.clrscreen()
        print("\t\t\t customer Record Management \n")
        print("==============================================================================")
        print("1.Ice Cream Sales Record")
        print("2.Display Sold Ice Cream Records")
        print("3.Update Ice Cream Sale")
        print("4.Return To Main Menu")
        print("==============================================================================")
        choice=int(input("Enter Choice Between 1 to 4  ----------> :"))
        if choice ==1:
            sales.insertsalesicecream()
        elif choice==2:
            sales.showsalesicecream()
        elif choice==3:
            sales.updatesalesicecream()
        elif choice==4:
            return
        else:
            print("Wrong Choice . . . . . . . . . .Enter Your Choice Again")
            x=input("enter any key to continue")
