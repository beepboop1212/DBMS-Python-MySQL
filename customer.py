#PYTHON MODULE: Customer

import mysql.connector

from mysql.connector import errorcode
from datetime import date,datetime,timedelta
from mysql.connector import(connection)
import os

def clrscreen():
    print('\n'*5)

def display():
    try:
        os.system('cls')
        cnx=connection.MySQLConnection(user='root',password='seq90',host='localhost',database='parlour')
        Cursor=cnx.cursor()
        query=("SELECT * FROM Customer")
        Cursor.execute(query)
        for(Cno,cname,mobno,doo,shopADR) in Cursor:
            print("===========================================================================")
            print("Customer Code:",Cno)
            print("Customer Name:",cname)
            print("mobile No. Of Customer:",mobno)
            print("Date Of order:",doo)
            print("Shop Address:",shopADR)
            print("===========================================================================")
        Cursor.close()
        cnx.close()
        print("You have done it !!!!!!!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()


def insertcustomer():
    try:
        cnx=connection.MySQLConnection(user='root',password='seq90',host='localhost',database='parlour')
        Cursor=cnx.cursor()
        Cno=input("Enter Customer Code:")
        cname=input("Enter Customer Name:")
        mobno=input("Enter Customer mobile No. :")
        print("Enter Date of order (Date /Month and year seperately:")
        DD=int(input("Enter Date:"))
        MM=int(input("Enter Month:"))
        YY=int(input("Enter Year:"))
        addr=input("Enter Customer Address:")
        Qry=("INSERT INTO Customer VALUES(%s,%s,%s,%s,%s)")
        data=(Cno,cname,mobno,date(YY,MM,DD),addr)
        Cursor.execute(Qry,data)
#Make sure data is committed to the database cnx.commit()
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Record inserted. . . . . . ")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
              print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
        else:
                print(err)
        cnx.close()


def deletecustomer():
    try:
        cnx=connection.MySQLConnection(user='root',password='seq90',host='localhost',database='parlour')
        Cursor=cnx.cursor()
        Cno=int(input("Enter Customer code to be deleted from the parlour:"))
        Qry=("""DELETE FROM Customer WHERE Custno = %s""")
        del_rec=(Cno,)
        Cursor.execute(Qry,del_rec)

    #Make sure data is committed to the database cnx.commit()
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount,"Record(s) Deleted Successfuly. . . . . . ")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
          print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()


def searchcustomer():
    try:
        cnx=connection.MySQLConnection(user='root',password='seq90',host='localhost',database='parlour')
        Cursor=cnx.cursor()
        mnm=input("Enter Customer Name to be Searched from parlour:")
        query=("SELECT * FROM Customer where cname=%s")
        rec_srch=(mnm,)
        Cursor.execute(query,rec_srch)
        Rec_count=0
        for (Cno,cname,mobno,doo,shopADR) in Cursor:
            print("=============================================================")
            print("Customer Code:",Cno)
            print("Customer Name:",cname)
            print("Mobile No. Of Customer:",mobno)
            print("Date Of order :",doo)
            print("Shop Address:",shopADR)
            print("=============================================================================")
            if Rec_count%2==0:
                input("Press any key to continue")
                clrscreen()
        print(Rec_count,"Record(s) found")
#make sure data is commited to the database cnx.commit()
        Cursor.close()
        cnx.close()

    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Datebase does not exist")
        else:
            print(err)
        cnx.close()






def updatecustomer():
    try:
        cnx=connection.MySQLConnection(user='root',password='seq90',host='localhost',database='parlour')
        Cursor=cnx.cursor()
        Cno=input("Enter Customer Code to update from the parlour:")
        query=("SELECT * FROM Customer where Cno=%s")
        rec_srch=(Cno,)
        print("Enter new data")
        Cno=input("Enter Customer Code:")
        cname=input("Enter Customer Name:")
        mobno=input("Enter Customer mobile No. :")
        print("Enter Date of Customership (Date /Month and year seperately:")
        DD=int(input("Enter Date:"))
        MM=int(input("Enter Month:"))
        YY=int(input("Enter Year:"))
        shopADR=input("Enter Shop Address:")
       
        Qry=("UPDATE Customer SET cname=%s,mobno=%s,d_o_visit =%s,shopADR=%s WHERE Custno=%s")
        data=(cname,mobno,date(year=YY,month=MM,day=DD),shopADR ,Cno)

        print(Cursor.rowcount,"Record(s) Updated Successfully. . . . . . .")     
        Cursor.execute(Qry,data)
    #Make sure data is comitted to the database cnx.commit()
        cnx.commit()
        Cursor.close()
        cnx.close()
        
                  
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                      print("Something is wrong with your user name  or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR: 
                      print("Database does not exist")
        else:
                 print(err)
        cnx.close()
        updatecustomer()






