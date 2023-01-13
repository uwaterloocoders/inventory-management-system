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
