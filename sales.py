#PYTHON MODULE: payment

import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import (connection)
import os

def clrscreen():
    print('\n'*5)

def showsalesicecream():
    try:
        os.system('cls')
        cnx=connection.MySQLConnection(user='root',password='seq90',
                                                           host='localhost',
                                                           database='parlour')
        Cursor=cnx.cursor()
        query=("SELECT B.iceid,B.icename,M.custno,M.cname ,I.dopayment, I.amount FROM icecream B,sales I, customer M where i.iceid=b.iceid  and I.custno=M.custno")
        Cursor.execute(query)
        for(iceid,icename,custno,cname,dopayment,amount) in Cursor:
            print("=======================================================")
            print("Ice Cream Code:",iceid)
            print("Ice Cream Name:",icename)
            print("Customer Code:",custno)
            print("Customer Name:",cname)
            print("Date of payment:",dopayment)
            print("Amount Paid",amount)
            print("========================================================")
        Cursor.close()
        cnx.close()
        print("You have done it !!!!!!")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
           print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
           print("Database does not exist")
        else:
           print(err)
    else:
        cnx.close()


def insertsalesicecream():
    try:
        cnx=connection.MySQLConnection(user='root',password='seq90', host='localhost',database='parlour')
        Cursor=cnx.cursor()
        iceid=input("Enter Ice Cream Code to be paid:")
        custno=input("Enter Customer Code:")
        print("Enter Date of payment(Date/month and year separately):")
        DD=int(input("Enter Date:"))
        MM=int(input("Enter Month:"))
        YY=int(input("Enter Year:"))
        amount=input("Enter Ice Cream amount:")
        Qry=("insert INTO sales(iceid, custno, dopayment,amount) VALUES (%s,%s,%s,%s)")
        data=(iceid, custno, date(YY,MM,DD), amount)
        Cursor.execute(Qry,data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("record inserted.................")
    except mysql.connector.Error as err :
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
              print("Something is wrong with your user name or password")
        elif err.errno==errorcode.ER_BAD_DB_ERROR:
              print("Database does not exist")
        else:
              print(err)
    cnx.close()

    
def updatesalesicecream():
      try:
              cnx=connection.MySQLConnection(user='root', password='seq90', host='localhost', database='parlour')
              Cursor=cnx.cursor() 
              iceid=int(input("Enter Ice Cream code of icecream sold in the parlour:"))
              custno=int(input("Enter customer code of the customer who is purchasing the icecream:"))
              amount=int(input("Enter icecream amount:"))
              Qry=("""update sales set amount=%s WHERE iceid=%s and custno=%s""")
              rec=(amount,iceid,custno)
              Cursor.execute(Qry,rec)
                   #make sure data is commited to the database
              print(Cursor.rowcount,"Record(s) Updated Succesfully..............")
              cnx.commit()
              Cursor.close()
              cnx.close()
             
      except mysql.connector.Error as err :
              if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
                      print("Something is wrong with your user name or password")
              elif err.errno==errorcode.ER_BAD_DB_ERROR:
                     print("Database does not exist")
              else:
                    print(err)
              cnx.close()

