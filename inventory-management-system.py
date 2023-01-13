from tabulate import tabulate
import mysql.connector
mydb=mysql.connector.connect(host="localhost", 
                           user="root", 
                           passwd=" ")
cur=mydb.cursor()

cur.execute("Create database Shop_Management")
cur.execute("show databases")
for i in cur:
    print(i)

cur.execute('create table SHOP( ItemNo integer(3), ItemName varchar(30), Quantity integer(5), Price integer(5))')

cur.execute("show tables")
for i in cur:
    print(i)

# ***** FUNCTIONS FOR INVENTORY ***** #
# Function for Adding Records

def additem():
    while True:
        print("\nContents in table SHOP")
        a=cur.execute("select * from Shop")
        cur.execute(a)
        print(tabulate(cur, headers =['ItemNo', 'ItemName', 'Quantity','Price'],tablefmt='psql'))
    
        print("\nADDING RECORDS ...")
        itno=int(input("\nEnter Item Number - "))
        itnm=input("Enter Item Name - ")
        qty=int(input("Enter Quantity - ")) 
        pr=int(input("Enter price - Rs. "))
        cur.execute("insert into shop values( {},'{}',{},{})".format(itno,itnm,qty,pr))
        mydb.commit()
        print("\nRecord Added Successfully !!!")

        abc=input("\nDo you want to Add more Records ? (y/n) - ")
        if abc=='n':
            break

# Function for Updating Records
def updateitem():

    print("\nContents in table SHOP")
    a=cur.execute("select * from Shop")
    cur.execute(a)
    print(tabulate(cur, headers =['ItemNo', 'ItemName', 'Quantity', 'Price'],tablefmt='psql'))

    try:
        print("\nUPDATING RECORDS ...")
        print('''\nWhat do you want to Update ? - 
        1. Item Name
        2. Quantity of an Item
        3. Price of an Item''')


        while True:
            
            ch=int(input("\nEnter your Choice - "))
            if ch==1:
                print("\nUPDATING ITEM NAME...")
                itemno=int(input("\nEnter Item Number - "))
                itemnm=input("Enter Updated Item Name - ")
                cur.execute("update shop set itemname = '{}'where itemno = {}".format(itemnm, itemno))
                mydb.commit()
                print("\nRecord Updated Successfully !!!")
            
            
            elif ch==2:
                print("\nUPDATING QUANTITY...")
                itemno=int(input("\nEnter Item Number - "))
                qty=int(input("Enter Updated Quantity - "))
                cur.execute("update shop set Quantity = {} where itemno = {}".format(qty,itemno))
                mydb.commit()
                print("\nRecord Updated Successfully !!!")

            elif ch==3:
                print("\nUPDATING PRICE...")
                itemno=int(input("\nEnter Item Number - "))
                pr=int(input("Enter Updated Price - "))
                cur.execute("update shop set Price = {} where itemno = {}".format(pr,itemno))
                mydb.commit()
                print("\nRecord Updated Successfully !!!")
                
            else:
                print("Please Enter a Valid Input")
                break

    except:
        print("Enter Valid Input")

        
# Function for Deleting Records
def delitem():
    
    while True:

        print("\nContents in table SHOP")
        a=cur.execute("select * from Shop")
        cur.execute(a)
        print(tabulate(cur, headers = ['ItemNo', 'ItemName', 'Quantity','Price'],tablefmt='psql'))


        ch=input("\nDo you want to continue to delete a Record ? (y/n) - ")
        
        if ch == 'y':
            itemno=int(input("\nEnter Item Number - "))
            cur.execute("delete from shop where itemno = {} " .format(itemno))
            mydb.commit()
            print("\nRecord Deleted Successfully !!!")
        
        else:
            print("Thanks!!!")
            break
