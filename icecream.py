#PYTHON MODULE:Icecream

import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
import os
import platform

def clrscreen():
    if platform.system()=="Windows":
        print(os.system("cls"))

def display():
    try:
        os.system('cls')
        cnx=connection.MySQLConnection(user='root',password='seq90',host='localhost',database='parlour')
        Cursor=cnx.cursor()
        query=("SELECT * FROM icecream")
        Cursor.execute(query)
                 
        for (iceid,icename,Company,price,publ,qty,d_o_manufac) in Cursor:
            print("==============================================================================")
            print("Ice Cream Code:",iceid)
            print("Ice Cream Name:",icename)
            print("Company Of Ice Cream:",Company)
            print("Price Of Ice Cream:",price)
            print("Flavour:",publ)
            print("Total Quantity In Hand:",qty)
            print("Delivered On",d_o_delivery)
            print("==============================================================================")
        Cursor.close()
        cnx.close()
        print("You have done it !!!!")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
            cnx.close()

import mysql.connector

def insertdata():
    try:
        cnx = connection.MySQLConnection(user='root',password='seq90',host='localhost',database='parlour')
        Cursor=cnx.cursor()
        iceid=input("Enter Ice Cream Code:")
        icename=input("Enter Ice Cream Name:")
        Auth=input("Enter Company's Name:")
        price=int(input("Enter Ice Cream Price:"))
        publ=input("Enter flavour Of The Ice Cream:")
        qty=int(input("Enter Quantity purchased:"))
        print("Enter Date of Purchase(Date/Month and Year seperately):")
        DD=int(input("Enter Date :"))   
        MM=int(input("Enter Month:"))
        YY=int(input("Enter Year:"))
        Qry=("INSERT INTO icecream VALUES (%s,%s,%s,%s,%s,%s,%s)")
        data=(iceid,icename,Auth,price,publ,qty,date(YY,MM,DD))
    #    data=(iceid,icename,Auth,price,price,publ,qty,date(YY,MM,DD))
        Cursor.execute(Qry,data)
        print("Record Inserted. . . . . . . . . . . . ")
        cnx.commit()
#Make sure data is commited to the database cnx.commit()
        Cursor.close()
        cnx.close()
        
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
        else:
                print(err)
    cnx.close()

def deleteicecream():
    try:
            cnx = connection.MySQLConnection(user='root',password='seq90',host='localhost',database='parlour')        
            Cursor = cnx.cursor()
            iceid=input("Enter Ice Cream Code of Ice Cream to be deleted from the parlour:")
            Qry=("""DELETE FROM icecream WHERE iceid = %s""")
            del_rec=(iceid,)
            Cursor.execute(Qry, del_rec)
                #Make sure data is commited to the database cnx.commit()
            print(Cursor.rowcount,"Record(s) Deleted Successfully. . . . . . . ")
            Cursor.close()
            cnx.commit()
            cnx.close()
    except mysql.connector.Error as err:
            if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno==errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
    cnx.close()


def updateicecream():
    try:
        cnx=connection.MySQLConnection(user='root',password='seq90',host='localhost',database='parlour')
        Cursor=cnx.cursor()
        iceid=input("Enter Ice Cream Code of Ice Cream to update from the parlour:")
        query=("SELECT * FROM icecream where iceid=%s")
        rec_srch=(iceid,)
        print("Enter new data")
        icename=input("Enter Ice Cream Name:")
        Auth=input("Enter Ice Cream Company:")
        price=int(input("Enter Ice Cream Price:"))
        publ=input("Enter flavour of Ice Cream:")
        qty=int(input("Enter Quantity purchased:"))
        print("Enter Date of Purchase (Date / month and year seperately:")
        DD=int(input("Enter Date:"))
        MM=int(input("Enter Month:"))
        YY=int(input("Enter Year:"))
        Qry=("UPDATE icecream SET icename=%s,Company=%s,price=%s,flavour=%s,qty = %s,d_o_delivery=%s WHERE iceid=%s")
        data=(icename,Auth,price,publ,qty,date(year=YY,month=MM,day=DD),iceid)
        Cursor.execute(Qry,data)

        print(Cursor.rowcount,"Record(s) Updated Successfully. . . . . . .")
    #Make sure data is comitted to the database
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
        updateicecream()

def searchicecreamrec():
    try:
        cnx=connection.MySQLConnection(user='root',password='seq90',host="localhost",database='parlour')
        Cursor=cnx.cursor()
        iceid=input("Enter Ice Cream No to be Searched from the parlour:")
        query=("SELECT * FROM icecream where iceid=%s")
        rec_srch=(iceid,)
        Cursor.execute(query,rec_srch)
        Rec_count=0
        for (iceid,icename,Company,price,publ,qty,d_o_delivery) in Cursor:
            Rec_count+=1
            print("==============================================================================")
            print("Ice Cream Code:",iceid)
            print("Ice Cream Name:",icename)
            print("Company Of Ice Cream:",Company)
            print("Price Of Ice Cream:",price)
            print("Flavour:",publ)
            print("Total Quantity In Hand:",qty)
            print("Purchased On",d_o_delivery)
            print("==============================================================================")
            if Rec_count%2==0:
                input("Press Any Key To Continue")
                clrscreen()
                print(Rec_count,"Record(s) fount")
#Make sure data is commited to the database cnx.commit()
        Cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
                          print("Something is wrong with your user name  or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR: 
                      print("Database does not exist")
        else:
            print(err)
    cnx.close()
    
                
            
